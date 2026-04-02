
## Configuration

This action validates GitHub Actions usage in workflow files and composite actions. It can enforce two independent controls:

- **Allowed usage** via `whitelist`
- **Pinning enforcement** via `exemptions`

`whitelist` determines which remote actions may be used in the repository at all. `exemptions` determines which actions are allowed to skip full SHA or digest pinning. These are intentionally separate so that an action can be allowed without also being exempt from pinning requirements.

### Inputs

| Input | Description | Default |
|---|---|---|
| `whitelist` | Newline-separated list of allowed owners or repositories. Use `actions/` to allow an owner prefix, or `actions/checkout` to allow a repository including any subpath. Empty means allow all. | `''` |
| `exemptions` | Newline-separated list of owners or repositories exempt from SHA or digest pinning enforcement. Empty means exempt none. | `''` |
| `dry_run` | When `true`, findings are emitted as warnings and the job does not fail. | `'false'` |
| `workflows-path` | Path to the workflows directory to scan. | `.github/workflows` |
| `actions-path` | Path to the composite actions directory to scan. | `.github/actions` |

## Rule Semantics

### Whitelist

The `whitelist` controls whether a remote action is permitted to be used.

- If `whitelist` is empty, all remote actions are allowed.
- If `whitelist` is non-empty, every remote action must match at least one rule.

### Exemptions

The `exemptions` input controls whether an allowed action may skip pinning enforcement.

- If `exemptions` is empty, no actions are exempt.
- If an action matches `exemptions`, it is still subject to `whitelist` checks.
- Exemptions do **not** bypass allowed-usage policy.

### Matching behavior

Rules support two formats:

- `owner/`  
  Matches all actions under that owner.

- `owner/repo`  
  Matches that repository, including any subpath within it.

Examples:

- `actions/` matches:
  - `actions/checkout`
  - `actions/setup-node`

- `github/codeql-action` matches:
  - `github/codeql-action/init`
  - `github/codeql-action/analyze`

## What Is Checked

The action scans:

- workflow job-level `uses` entries for reusable workflows
- workflow step-level `uses` entries
- composite action step-level `uses` entries

It validates the following:

- local references such as `./.github/actions/foo` are ignored
- remote GitHub actions and reusable workflows must include an `@ref`
- non-exempt remote actions must be pinned to a full 40-character commit SHA
- non-exempt `docker://` references must be pinned to a `sha256` digest

## Examples

### Enforce full SHA pinning for everything

This is the strictest mode.

```yaml
- name: Validate GitHub Actions usage
  uses: ./.github/actions/ensure-sha-pinned-actions
  with:
    dry_run: false
````

Behavior:

* all remote actions are allowed
* all remote actions must be pinned to a full commit SHA
* all `docker://` references must be pinned to a digest
* nothing is exempt

### Only allow actions from a specific owner

```yaml
- name: Validate GitHub Actions usage
  uses: ./.github/actions/ensure-sha-pinned-actions
  with:
    whitelist: |
      actions/
```

Behavior:

* only actions under the `actions` owner are allowed
* they must still be pinned unless also exempted

### Allow only specific repositories

```yaml
- name: Validate GitHub Actions usage
  uses: ./.github/actions/ensure-sha-pinned-actions
  with:
    whitelist: |
      actions/checkout
      actions/setup-node
      github/codeql-action
```

Behavior:

* only those repositories may be used
* subpaths in those repositories are also allowed
* all must still be pinned unless exempted

### Exempt selected actions from pinning

```yaml
- name: Validate GitHub Actions usage
  uses: ./.github/actions/ensure-sha-pinned-actions
  with:
    exemptions: |
      actions/checkout
      actions/setup-node
```

Behavior:

* all actions are allowed
* `actions/checkout` and `actions/setup-node` may use tag refs such as `@v4`
* everything else must still be pinned

### Combine whitelist and exemptions

```yaml
- name: Validate GitHub Actions usage
  uses: ./.github/actions/ensure-sha-pinned-actions
  with:
    whitelist: |
      actions/
      github/codeql-action
    exemptions: |
      actions/checkout
```

Behavior:

* only `actions/*` and `github/codeql-action` are allowed
* `actions/checkout` is allowed and exempt from pinning
* other allowed actions must still be pinned

### Run in advisory mode

```yaml
- name: Validate GitHub Actions usage
  uses: ./.github/actions/ensure-sha-pinned-actions
  with:
    dry_run: true
```

Behavior:

* findings are emitted as warnings
* the job does not fail

## Expected Results

| `uses:` value                                                                             | whitelist              | exemptions         | Result |
| ----------------------------------------------------------------------------------------- | ---------------------- | ------------------ | ------ |
| `actions/checkout@8ade135a41bc03ea155e62e844d188df1ea18608`                               | empty                  | empty              | Pass   |
| `actions/checkout@v4`                                                                     | empty                  | empty              | Fail   |
| `actions/checkout@v4`                                                                     | `actions/checkout`     | empty              | Fail   |
| `actions/checkout@v4`                                                                     | `actions/checkout`     | `actions/checkout` | Pass   |
| `actions/setup-node@main`                                                                 | `actions/`             | empty              | Fail   |
| `github/codeql-action/analyze@f3c623b6e9d9f0c2b4d2d8a5e2f7c4a1b6e8d123`                   | `github/codeql-action` | empty              | Pass   |
| `docker://alpine:3.19`                                                                    | empty                  | empty              | Fail   |
| `docker://alpine@sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef` | empty                  | empty              | Pass   |
| `some-owner/some-action@1234567890123456789012345678901234567890`                         | `actions/`             | empty              | Fail   |
| `./.github/actions/my-local-action`                                                       | any                    | any                | Pass   |

## Notes

* Use `whitelist` to define what is allowed in the repository.
* Use `exemptions` only for actions that are intentionally permitted to avoid pinning checks.
* Keeping these controls separate makes the policy easier to reason about and avoids accidentally turning “allowed” into “ignored.” 

