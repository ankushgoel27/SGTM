import json
import src.github.webhook as github_webhook


def handler(event: dict, context: dict) -> None:
    if "headers" not in event:
        raise KeyError(
            "Expected there to be headers in the event. Keys were: {}".format(
                event.keys()
            )
        )

    event_type = event["headers"].get("X-GitHub-Event")

    if not event_type:
        raise KeyError("Expected a X-GitHub-Event header, but none found")

    github_event = json.loads(event["body"])
    return github_webhook.handle_github_webhook(event_type, github_event)
