# Prompt Injection Guard

A GitHub Action that scans text for prompt injection attacks using [Llama Prompt Guard 2](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M) from Meta.

## Overview

This action uses Meta's Llama Prompt Guard 2 model to detect:
- **Prompt injection attacks** - attempts to override system instructions
- **Jailbreak attempts** - attempts to bypass safety restrictions

The model runs on CPU within the GitHub Actions runner, with caching for faster subsequent runs.

## Usage

### Basic Usage

```yaml
- name: Check for prompt injection
  uses: MakerXStudio/shared-config/.github/actions/prompt-injection-guard@main
  with:
    text: |
      ${{ github.event.issue.title }}
      ${{ github.event.issue.body }}
    huggingface-token: ${{ secrets.HF_TOKEN }}
```

### With Claude Code Action

```yaml
jobs:
  process-issue:
    runs-on: ubuntu-latest
    steps:
      - name: Check for prompt injection
        uses: MakerXStudio/shared-config/.github/actions/prompt-injection-guard@main
        with:
          text: |
            ${{ github.event.issue.title }}
            ${{ github.event.issue.body }}
          huggingface-token: ${{ secrets.HF_TOKEN }}

      # Only runs if the above step passes
      - name: Run Claude Code
        uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Custom Threshold

```yaml
- name: Check for prompt injection
  uses: MakerXStudio/shared-config/.github/actions/prompt-injection-guard@main
  with:
    text: ${{ github.event.comment.body }}
    huggingface-token: ${{ secrets.HF_TOKEN }}
    threshold: '0.7'  # Higher threshold = fewer false positives
```

### Using the Smaller Model

```yaml
- name: Check for prompt injection
  uses: MakerXStudio/shared-config/.github/actions/prompt-injection-guard@main
  with:
    text: ${{ github.event.issue.body }}
    huggingface-token: ${{ secrets.HF_TOKEN }}
    model: '22M'  # Faster but slightly less accurate
```

### Non-blocking Mode

```yaml
- name: Check for prompt injection
  id: injection-check
  uses: MakerXStudio/shared-config/.github/actions/prompt-injection-guard@main
  with:
    text: ${{ github.event.issue.body }}
    huggingface-token: ${{ secrets.HF_TOKEN }}
    fail-on-malicious: 'false'

- name: Log result
  run: |
    echo "Classification: ${{ steps.injection-check.outputs.classification }}"
    echo "Confidence: ${{ steps.injection-check.outputs.confidence }}"
    echo "Is malicious: ${{ steps.injection-check.outputs.is-malicious }}"
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `text` | The text to scan for prompt injection attacks | Yes | - |
| `huggingface-token` | HuggingFace token for accessing the gated model | Yes | - |
| `model` | Model size to use (`86M` or `22M`) | No | `86M` |
| `threshold` | Confidence threshold for MALICIOUS classification (0.0-1.0) | No | `0.5` |
| `fail-on-malicious` | Whether to fail the action if malicious content is detected | No | `true` |

## Outputs

| Output | Description |
|--------|-------------|
| `classification` | Classification result (`BENIGN` or `MALICIOUS`) |
| `confidence` | Confidence score (0.0-1.0) |
| `is-malicious` | Whether the text was classified as malicious (`true`/`false`) |

## Setup

### HuggingFace Token

The Llama Prompt Guard 2 model is gated and requires a HuggingFace account:

1. Create a [HuggingFace account](https://huggingface.co/join)
2. Accept the model license at [meta-llama/Llama-Prompt-Guard-2-86M](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M)
3. Create an access token at [HuggingFace Settings](https://huggingface.co/settings/tokens)
4. Add the token as a repository secret named `HF_TOKEN`

## Performance

| Metric | 86M Model | 22M Model |
|--------|-----------|-----------|
| Cold start | ~45-60s | ~30-40s |
| Warm start (cached) | ~10-15s | ~8-12s |
| Inference per chunk | ~100-200ms | ~50-100ms |

The action caches both Python dependencies and the model weights, significantly reducing startup time on subsequent runs.

## Model Details

### What it Detects

- Direct injection attempts ("Ignore previous instructions...")
- Jailbreak patterns ("You are now in developer mode...")
- Encoded/obfuscated commands
- Role-play bypass attempts
- Multi-language attacks (86M model)

### Limitations

- 512 token context window (longer texts are chunked)
- May not catch all sophisticated attacks
- Does not detect indirect injection (e.g., from fetched URLs)
- No conversation context (single-text classification only)

## License

This action uses the [Llama Prompt Guard 2](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M) model, which is released under the [Llama 3.2 Community License](https://www.llama.com/llama3_2/license/).
