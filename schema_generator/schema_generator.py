from drf_yasg.generators import OpenAPISchemaGenerator

class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        swagger = super().get_schema(request, public)

        swagger.schemes = ['https', 'http']
        swagger.tags = [
            {
                "name": "users",
                "description": "Authentication API. This API contain endpoints to register, login  and user data",
            },
            {
                "name": "posts",
                "description": "Users can create posts, retrieve their posts and other users posts, update and delete their own posts. They can also like and unlike other users' posts",
            },
        ]
        return swagger

