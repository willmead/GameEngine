from kobold.components import Component


class Entity:
    
    def __init__(self) -> None:
        self.components = []

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def has_component(self, name: str) -> bool:
        return name in [component.name for component in self.components]
    
    def get_component(self, name: str) -> Component:
        for component in self.components:
            if component.name == name:
                return component
        return None
    