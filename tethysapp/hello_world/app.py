from tethys_sdk.base import TethysAppBase, url_map_maker


class HelloWorld(TethysAppBase):
    """
    Tethys app class for Hello World.
    """

    name = 'Hello World'
    index = 'hello_world:home'
    icon = 'hello_world/images/icon.gif'
    package = 'hello_world'
    root_url = 'hello-world'
    color = '#2eba0e'
    description = 'My first Tethys App'
    tags = '&quot;first app&quot;, &quot;learning&quot;, &quot;o ye hypocrites&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hello-world',
                controller='hello_world.controllers.home'
            ),
        )

        return url_maps
