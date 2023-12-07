import json
from odoo import http
from odoo.http import request, Response


class VehicleCurrentLocation(http.Controller):
    # get: /api/v1/vehicleLocation
    @http.route(
        "/api/v1/vehicleLocations",
        methods=["GET"],
        type="http",
        auth="public",
        website=True,
    )
    def get_vehicle_location(self):
        serialized_response = []
        vehicle_current_coordinates = request.env["revision.schema"].sudo().search([])

        for record in vehicle_current_coordinates:
            serialized_data = {
                "first_name": record.first_name,
                "last_name": record.surname,
            }
            serialized_response.append(serialized_data)

        # print(response)
        # return Response(json.dumps(response), content_type="application/json")
        # print(data)
        return Response(
            json.dumps(serialized_response), content_type="application/json"
        )

    # post: /api/v1/vehicleLocation/create
    @http.route(
        "/api/v1/vehicleLocations/create",
        type="http",
        methods=["POST"],
        auth="public",
        website=True,
        csrf=False,
        cors="*",
    )
    def create_vehicle_locations(self, **kwargs):
        try:
            request_json = json.loads(http.request.httprequest.data)
            first_name = request_json.get("first_name")
            last_name = request_json.get("surname")
            # print(first_name,last_name)

            # Create a new record in the 'revision.schema' model
            new_vehicle_location = (
                http.request.env["revision.schema"]
                .sudo()
                .create({"first_name": first_name, "surname": last_name})
            )

            # Return the response with the newly inserted vehicle location data
            return http.Response(
                json.dumps(
                    {
                        "id": new_vehicle_location.id,
                        "first_name": new_vehicle_location.first_name,
                        "last_name": new_vehicle_location.surname,
                    }
                ),
                content_type="application/json",
            )
        except Exception as e:
            return http.Response(
                json.dumps({"error": str(e)}),
                status=400,  # Bad Request status code
                content_type="application/json",
            )

    # get: /api/v1/vehicleLocations/{id}
    @http.route(
        "/api/v1/vehicleLocations/<int:id>",
        methods=["GET"],
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def get_vehicle_location(self, id, **kwargs):
        vehicle_location = (
            http.request.env["revision.schema"]
            .sudo()
            .search([("id", "=", id)], limit=1)
        )

        # Check if location is found
        if vehicle_location:
            vehicle_location_response = {
                "id": vehicle_location.id,
                "first_name": vehicle_location.first_name,
                "last_name": vehicle_location.surname,
            }

            return http.Response(
                json.dumps(vehicle_location_response), content_type="application/json"
            )
        else:
            # Return 404 response if record is not found
            return http.Response(
                json.dumps({"error": "Record Not Found"}),
                status=404,
                content_type="application/json",
            )
