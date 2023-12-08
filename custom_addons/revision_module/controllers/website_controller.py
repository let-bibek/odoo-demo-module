from odoo import http
from odoo.http import request, Response
import json


class WebsiteController(http.Controller):
    # route: get: /user_registration
    @http.route("/user_registration", auth="public", csrf=False, website=True, cors="*")
    def user_registration_url(self):
        return request.render("revision_module.vehicle_request_template", {})

    # get: /user_registration/create
    @http.route(
        "/user_registration/create",
        methods=["POST"],
        auth="public",
        website=True,
        csrf=False,
        cors="*",
    )
    def user_registration(self, **kwargs):
        # Access user request contents
        # request_json = json.loads(http.request.httprequest.data)
        user_name = kwargs.get("username")
        email = kwargs.get("email")

        # Insert into the database
        new_user = (
            http.request.env["revision.schema"]
            .sudo()
            .create({"first_name": user_name, "email": email})
        )
        return http.Response(
            json.dumps(
                {
                    "id": new_user.id,
                    "registered_user_name": new_user.first_name,
                    "email": new_user.email,
                }
            ),
            content_type="application/json",
        )
