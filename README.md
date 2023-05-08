# MakerX Shared Config
A collection of MakerX reusable workflows and configs.

## GitHub - Zendesk integration
The zendesk github integration consist of 3 github actions.
- [github_zendesk_issue_labelled.yml](.github/workflows/github_zendesk_issue_labelled.yml)
- [github_zendesk_issue_commented.yml](.github/workflows/github_zendesk_issue_commented.yml)
- [github_zendesk_issue_closed.yml](.github/workflows/github_zendesk_issue_closed.yml)

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
The workflows need to be added to each repository that we want to sync issues to Zendesk. However, to avoid repeat code, they can also be reused via [Calling a reusable workflow](https://docs.github.com/en/actions/learn-github-actions/reusing-workflows#calling-a-reusable-workflow). Samples can be found [here](samples/github-zendesk-integration-workflows/).

### Limitations
There are known limitation of GitHub - Zendesk integration:
- Markdown comments aren't supported due to an issue with Zendesk API.
- When an issue is created, existing comments aren't synced to Zendesk.
- Comment updates aren't synced to Zendesk.
- Removing issue label from GitHub doesn't have an affect, the corresponding Zendesk ticket is still need to be handled manually.
- The GitHub actions don't have retry logic, if they failed, the data won't be synced.

## Zendesk - GitHub integration
Zendesk - GitHub integration is done via webhook and Zendesk events. Zendesk events will trigger GitHub workflows of a GitHub repository (let's call it the entry point). From this entry point, it works out the target repository for dispatching workflows. Currently, there are:
- [zendesk_github_ticket_commented.yml](.github/workflows/zendesk_github_ticket_commented.yml)
- [zendesk_github_ticket_solved.yml](.github/workflows/zendesk_github_ticket_solved.yml)

### Setup Zendesk webhook
You can find the Postman collection for Zendesk API [here](postman/Zendesk%20API/). Import the collection and the global variables to your local postman. There are some variables to set:
- zendesk-tenant-name: Zendesk tenant name (it also is called subdomain), can be found in the URL. For example, for https://my-subdomain.zendesk.com/, it's my-subdomain
- zendesk-auth-token: Zendesk auth token. See https://support.zendesk.com/hc/en-us/articles/115000510267-How-can-I-authenticate-API-requests-#heading2
- zendesk-webhook-id: Zendesk webhook Id, we will set that later
- github-owner: GitHub repository owner
- github-repo: The repository which Zendesk will trigger the workflow from
- github-pat: GitHub personal access token, it needs to have repository permission `contents:write` to the entry point repository

Steps:
- Run `Create webhook` API to create the Zendesk webhook. Remember to take note of the response `id` and set the `zendesk-webhook-id` variable.
- Run `Create trigger - ticket solved` API
- Run `Create trigger - ticket commented` API

### Integration
From GitHub side, there are:
- [zendesk_github_add_comment.yml](.github/workflows/zendesk_github_add_comment.yml)
- [zendesk_github_close_issue.yml](.github/workflows/zendesk_github_close_issue.yml)

They will be invoked by `zendesk_github_ticket_commented` and `zendesk_github_ticket_solved` respectively. They need to be added to each repository that we want to sync comments and statuses from Zendesk. However, to avoid repeat code, they can also be reused via [Calling a reusable workflow](https://docs.github.com/en/actions/learn-github-actions/reusing-workflows#calling-a-reusable-workflow). Samples can be found [here](samples/zendesk-github-integration-workflows/).

Zendesk - GitHub integration needs `GH_ZENDESK_INVOKE_WORKFLOW_TOKEN` secrets to invoke the workflows. It's a personal access token, the only requirement is to have permission `contents:write` to any repository that we want to sync from Zendesk.