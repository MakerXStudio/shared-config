# Prepare Artifact Action

A reusable GitHub action that downloads artifacts, unzips them, and performs static site transforms. This action is based on the functionality from the [`node-deploy-cdk`](../node-deploy-cdk/action.yml) action but made more generic and reusable.

## Features

- Downloads all artifacts from the current workflow run
- Unzips artifacts to specified destinations
- Applies static site transforms (placeholder replacement) to files
- Supports multiple file extensions for transforms
- Handles both zip files and directory artifacts
- Provides detailed logging for troubleshooting

## Usage

### Basic Usage

```yaml
- name: Prepare artifacts
  uses: ./.github/actions/prepare-artifact
  with:
    app-artifact-unzips: |
      website:website/build
      app:app/dist
```

### With Static Site Transforms

```yaml
- name: Prepare artifacts with transforms
  uses: ./.github/actions/prepare-artifact
  with:
    app-artifact-unzips: |
      website:website/build
      app:app/dist
      poller:poller/build
    static-site-transforms: |
      VITE_API_ENDPOINT:${{ secrets.API_ENDPOINT }}
      VITE_CLIENT_ID:${{ secrets.CLIENT_ID }}
      VITE_TENANT_ID:${{ secrets.TENANT_ID }}
```

### Full Configuration

```yaml
- name: Prepare artifacts with custom settings
  uses: ./.github/actions/prepare-artifact
  with:
    app-artifact-unzips: |
      website:website/build
      app:app/dist
      poller:poller/build
    static-site-transforms: |
      VITE_API_ENDPOINT:${{ secrets.API_ENDPOINT }}
      VITE_CLIENT_ID:${{ secrets.CLIENT_ID }}
      VITE_TENANT_ID:${{ secrets.TENANT_ID }}
    artifacts-path: build-artifacts
    file-extensions: "*.js *.html *.css *.json *.ts"
```

## Inputs

### Required

- **`app-artifact-unzips`** (required): One or more lines of colon-separated pairs indicating:
  - A) artifact name 
  - B) destination folder where the artifact is unzipped
  
  Example:
  ```yaml
  app-artifact-unzips: |
    website:website/build
    app:app/dist
    poller:poller/build
  ```

### Optional

- **`static-site-transforms`** (optional): One or more lines of colon-separated pairs indicating:
  - A) placeholder variable value used in static site build
  - B) secret value to replace placeholder value with throughout the build
  
  Example:
  ```yaml
  static-site-transforms: |
    VITE_MAKER_GRAPH_API_ENDPOINT:https://api.example.com
    VITE_CLIENT_ID:your-client-id
    VITE_TENANT_ID:your-tenant-id
  ```

- **`artifacts-path`** (optional, default: `artifacts`): Path where artifacts are downloaded

- **`file-extensions`** (optional, default: `"*.js *.html *.css *.json"`): File extensions to apply transforms to (space separated)

## How It Works

1. **Download Artifacts**: Uses `actions/download-artifact@v4` to download all artifacts from the current workflow run to the specified `artifacts-path`.

2. **Process Artifact Unzips**: For each entry in `app-artifact-unzips`:
   - Creates the destination directory
   - Checks if the artifact exists as a zip file (`artifact-name.zip`)
   - If zip exists, unzips it to the destination
   - If no zip but directory exists, copies the directory contents
   - Logs warnings for missing artifacts

3. **Apply Static Site Transforms**: If `static-site-transforms` is provided:
   - Parses the placeholder:value pairs
   - Creates sed replacement commands
   - Applies transforms to files matching the specified extensions
   - Uses case-insensitive replacement for placeholders in `{{placeholder}}` format

## Example Workflow

```yaml
name: Deploy Application

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build website
        uses: ./.github/workflows/node-build-zip.yml
        with:
          artifact-name: website
          static-site: true
          
      - name: Build app
        uses: ./.github/workflows/node-build-zip.yml
        with:
          artifact-name: app
          working-directory: ./app

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Prepare artifacts
        uses: ./.github/actions/prepare-artifact
        with:
          app-artifact-unzips: |
            website:website/build
            app:app/dist
          static-site-transforms: |
            VITE_API_ENDPOINT:${{ secrets.API_ENDPOINT }}
            VITE_CLIENT_ID:${{ secrets.CLIENT_ID }}
```

## Comparison with node-deploy-cdk

This action extracts the artifact download, unzip, and transform functionality from the [`node-deploy-cdk`](../node-deploy-cdk/action.yml) action, making it reusable for scenarios where you need these operations without the CDK deployment steps.

### Key Differences

- **Focused scope**: Only handles artifact processing, not CDK deployment
- **More flexible**: Can be used with any deployment target
- **Enhanced logging**: Better error messages and progress tracking
- **Input validation**: Improved handling of malformed inputs
- **Directory support**: Handles both zip files and directory artifacts

### Migration from node-deploy-cdk

If you're using `node-deploy-cdk` and want to separate the artifact processing:

```yaml
# Before (node-deploy-cdk)
- name: Deploy CDK
  uses: ./.github/actions/node-deploy-cdk
  with:
    app-artifact-unzips: |
      website:website/build
    static-site-transforms: |
      VITE_API_ENDPOINT:${{ secrets.API_ENDPOINT }}
    # ... other CDK-specific inputs

# After (separated)
- name: Prepare artifacts
  uses: ./.github/actions/prepare-artifact
  with:
    app-artifact-unzips: |
      website:website/build
    static-site-transforms: |
      VITE_API_ENDPOINT:${{ secrets.API_ENDPOINT }}

- name: Deploy CDK
  uses: ./.github/actions/node-deploy-cdk
  with:
    # ... CDK-specific inputs only
```

## Error Handling

The action includes comprehensive error handling:

- **Missing artifacts**: Logs warnings but continues processing other artifacts
- **Invalid input format**: Logs warnings for malformed artifact unzip entries
- **Transform failures**: Continues processing if transforms fail on individual files
- **Directory creation**: Automatically creates destination directories

## Security Considerations

- **Secret values**: The action logs `[REDACTED]` instead of actual secret values
- **Input validation**: Validates input format to prevent injection attacks
- **File permissions**: Preserves file permissions when copying/extracting