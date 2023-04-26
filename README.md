# MakerX Shared Config
A collection of MakerX reusable workflows and configs.

## Zendesk integration
The zendesk github integration consist of 3 github actions.
- [zendesk_integration_issue_labelled.yml](.github/workflows/zendesk_integration_issue_labelled.yml)
- [zendesk_integration_issue_commented.yml](.github/workflows/zendesk_integration_issue_commented.yml)
- [zendesk_integration_issue_closed.yml](.github/workflows/zendesk_integration_issue_closed.yml)

### Issue labelled

Once an issue is assigned a specified label, it is sent to Zendesk,
creating (or using) the user `<Github UserName>` with email `<Github UserName>@users.noreply.github.com`.
This mail adress format is also used by github when a user sets the privacy option that the mail should be hidden.
Once the ticket got created a comment to the issue will be added to inform the user about the tech support contact.

### Issue commented

Every comment on an issue gets send to zendesk. It will look up the connected ticket and author and attaches the comment to the ticket.

### Issue closed

When an issue is closed, it is marked as solved in Zendesk.

### Integration
The workflows can also be reused via [Calling a reusable workflow](https://docs.github.com/en/actions/learn-github-actions/reusing-workflows#calling-a-reusable-workflow).

```
on:
  issue_comment:
    types: [labeled]
jobs:
  issue_created:
    uses: makerxstudio/shared-config/.github/workflows/zendesk_integration_issue_labelled.yml@main
    inputs:
      ZENDESK_TENANT_NAME: {tenant_name}
      ISSUE_LABEL: {issue label}
    secrets:
      ZENDESK_BASIC_AUTH: ${{ secrets.ZENDESK_BASIC_AUTH }}
```

### Limitations
There are known limitation of GitHub - Zendesk integration:
- Markdown comments aren't supported due to an issue with Zendesk API.
- When an issue is created, existing comments aren't synced to Zendesk.
- Comment updates aren't synced to Zendesk.
- Removing issue label from GitHub doesn't have an affect, the corresponding Zendesk ticket is still need to be handled manually.
- The GitHub actions don't have retry logic, if they failed, the data won't be synced.