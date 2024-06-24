import inspect
from typing import Text, Callable, Awaitable

from rasa.core.channels.channel import (
	InputChannel,
	CollectingOutputChannel,
	UserMessage,
)
from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse


class Discord(InputChannel):
	def name(self) -> Text:
		"""Name of your custom channel."""
		return "discord"

	def blueprint(
		self, on_new_message: Callable[[UserMessage], Awaitable[None]]
	) -> Blueprint:
		custom_webhook = Blueprint(
			type(self).__name__,
			inspect.getmodule(self).__name__,
		)

		@custom_webhook.route("/", methods=["GET"])
		async def health(request: Request) -> HTTPResponse:
			return response.json({"status": "ok"})

		@custom_webhook.route("/webhook", methods=["POST"])
		async def receive(request: Request) -> HTTPResponse:
			sender_id = request.json.get("sender")  
			text = request.json.get("text")  
			input_channel = self.name()  
			metadata = self.get_metadata(request)  

			collector = CollectingOutputChannel()
			await on_new_message(
				UserMessage(
					text,
					collector,
					sender_id,
					input_channel=input_channel,
					metadata=metadata,
				)
			)

			return response.json(collector.messages)

		return custom_webhook
