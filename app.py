from viktor import ViktorController
from viktor.parametrization import ViktorParametrization
from viktor.parametrization import NumberField, Text
from viktor.geometry import CircularExtrusion, Group, Material, Color, Point, LinearPattern, Line
from viktor.views import GeometryView, GeometryResult

class Parametrization(ViktorParametrization):
    ptext_building = Text('## Building dimensions')
    building_diameter = NumberField('Building diameter', min=10, default=20)
    building_floors = NumberField('Number of floors', min=3, default=10)


class Controller(ViktorController):
    label = 'My Entity Type'
    parametrization = Parametrization

    @GeometryView("3D model", duration_guess=1, x_axis_to_right=True)
    def starter_guide_model(self, params, **kwargs):
        floor_glass = CircularExtrusion(
            diameter=params.building_diameter,
            line=Line(Point(0, 0, 0), Point(0, 0, 2)),
            material=Material("Glass", color=Color(150, 150, 255))
        )
        floor_facade = CircularExtrusion(
            diameter=params.building_diameter+1,
            line=Line(Point(0, 0, 0), Point(0, 0, 1)),
            material=Material("Concrete", color=Color(200, 200, 200))
        )
        floor_facade.translate((0, 0, 2))
        floor = Group([floor_glass, floor_facade])
        building = LinearPattern(floor, direction=[0, 0, 1], number_of_elements=params.building_floors, spacing=3)
        return GeometryResult(geometry=building)
    