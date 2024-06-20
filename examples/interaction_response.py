from vortexkit import App, Request, JSONResponse
from dishookr import InteractionResponse, InteractionCallbackMessage, InteractionResponseType

"""
    - This is an example of how to use the InteractionResponse class to create an interaction response object that is fully accepted by Discord.
    - This InteractionResponse object is used in response to a discord interaction, received from a discord interaction callback.
    - This webserver is ran by VortexKit, a lightweight web framework.
"""

app = App()

@app.route("/interaction-callback")
def interaction_callback(request: Request):
    if not request.method == "POST":
        return JSONResponse({"error": "Method not allowed"}, status_code=405)
    
    if not type(request.body) == dict:
        return JSONResponse({"error": "Request body must be JSON"}, status_code=400)
    
    if request.body["type"] not in range(1,10):
        return JSONResponse({"error": "Invalid interaction type"}, status_code=400)
    
    # Handle the button click with custom_id of "button1"
    if request.body["type"] == 3 and request.body["data"]["custom_id"] == "button1":

        my_dishook_response = InteractionResponse(
                type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                data=InteractionCallbackMessage(
                    content="You clicked the button!"
                )
            )

        return JSONResponse(
            my_dishook_response.__dict__()
        )

    return JSONResponse({"error": "Invalid interaction type"}, status_code=400)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
