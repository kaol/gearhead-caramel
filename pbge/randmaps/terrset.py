from rooms import Room
from .. import container,scenes
import inspect

class TerrSet( Room ):
    # A Terrainset is a handler for TerrSetTerrain terrain.
    # Terrain Type is the TerrSetTerrain to be used.
    # TerrainMap is a tuple of tuples giving frame numbers for
    # the tiles. If a tile is to be left out, use None.
    TERRAIN_TYPE = None
    TERRAIN_MAP = (
        (None,None,None),
        (None,None),
        (None,None,None),
    )
    WAYPOINT_POS = dict()
    def __init__(self,tags=(), anchor=None, parent=None, archi=None, waypoints=dict()):
        self.width = max([len(a) for a in self.TERRAIN_MAP])
        self.height = len(self.TERRAIN_MAP)
        self.tags = tags
        self.anchor = anchor
        self.archi = archi
        self.area = None
        self.contents = container.ContainerList(owner=self)
        self.waypoints = dict()
        self.waypoints.update(waypoints)
        if parent:
            parent.contents.append( self )

    def build( self, scene, archi):
        # x0,y0 is the NorthWest corner of the terrain.
        x0,y0 = self.area.topleft
        y = y0
        for row in self.TERRAIN_MAP:
            x = x0
            for col in row:
                if scene.on_the_map(x,y) and col is not None:
                    if inspect.isclass( col ) and issubclass(col,scenes.terrain.Terrain):
                        scene._map[x][y].wall = col
                    else:
                        scene._map[x][y].wall = self.TERRAIN_TYPE
                        scene.data[(x,y)] = col
                x += 1
            y += 1
        for k,v in self.waypoints.iteritems():
            x,y = self.WAYPOINT_POS.get(k,(0,0))
            x += x0
            y += y0
            v.place(scene,(x,y))


