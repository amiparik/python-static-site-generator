import typer
from ssg.site import Site

    def main(source="content",dest="dist"):
        config = {"source":source,"dest":dest}
        site = Site(**cofig)

typer.run(main)
