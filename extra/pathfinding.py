from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import pygame
from typing import List, Tuple, Union

"""
Contains the PathFinder class.
"""

# PATHFINING


class PathFinder():
    """
    A useful pathfinding class to easly find paths for your sprites and making them follow the path.
    """

    def __init__(self, matrix: List[List[int]], cell_pixel_size: int, allow_diagonal_movement: bool = True):
        self.matrix = matrix

        for row in self.matrix:
            for col in row:
                if col not in [0, 1]:
                    raise ValueError("Matrix values must be either 0 or 1.")

        self.grid = Grid(len(self.matrix[0]), len(self.matrix), self.matrix)
        self.width = len(self.matrix[0])
        self.height = len(self.matrix)
        self.cell_size = cell_pixel_size
        if allow_diagonal_movement:
            self.finder = AStarFinder(
                diagonal_movement=DiagonalMovement.always)
        else:
            self.finder = AStarFinder()
        self.current_path = []
        self.collision_rects = []

    def ValidateTarget(self, target_grid_coordinate: Tuple[int, int]) -> bool:
        """
        Check if a position is inside the grid and if the node is not a wall.
        """
        if 0 <= target_grid_coordinate[0] <= self.width-1 and 0 <= target_grid_coordinate[1] <= self.height-1:
            if self.matrix[target_grid_coordinate[1]][target_grid_coordinate[0]] != 0:
                return True
        return False

    def GetDirectionForSprite(self,position:tuple|pygame.Vector2)->pygame.Vector2:
        """
        Get a direction to use for a moving sprite.
        """
        if self.collision_rects:
            start = pygame.math.Vector2(position)
            end = pygame.math.Vector2(self.collision_rects[0].center)
            try:
                return (end-start).normalize()
            except:
                return pygame.math.Vector2()
        else:
            return pygame.math.Vector2()

    def CheckSpriteOnPath(self, sprite)->pygame.Vector2|None|bool:
        """
        Checks if the sprite collided with a path point, in that case return the direction to the new point so the user can move the sprite appropriately.\n
        Return None if there is no collision, return True if the path is finished
        """
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(sprite.rect.center):
                    del self.collision_rects[0]
                    return self.GetDirectionForSprite(sprite.rect.center)
        else:
            if self.current_path:
                self.EmptyPath()
            return True
        return None

    def EmptyPath(self):
        """
        Clear the path and the collision rects.
        """
        self.current_path.clear()
        self.collision_rects.clear()

    def CreatePathCollisionRects(self, rect_size: int = 4) -> List[pygame.Rect]:
        """
        Create collision rects in the path points to allow sprites to follow it.
        """
        self.collision_rects.clear()
        if self.current_path:
            self.collision_rects = [pygame.Rect(((point[0]*self.cell_size)+self.cell_size//2-rect_size//2, (point[1]
                                                * self.cell_size)+self.cell_size//2-rect_size//2), (rect_size, rect_size)) for point in self.current_path]
        return self.collision_rects

    def DrawPath(self, surface: pygame.Surface, color: Union[str, Tuple[int, int, int]] = "white", line_width: int = 3, shift_offset: Union[str, int] = "cell_center"):
        """
        Draw the path if one exists.
        """
        if len(self.current_path) > 1:
            if shift_offset == "cell_center":
                shift_offset = self.cell_size//2
            points = [((point[0]*self.cell_size)+shift_offset, (point[1]
                       * self.cell_size)+shift_offset) for point in self.current_path]
            pygame.draw.lines(surface, color, False, points, line_width)

    def GridToPixel(self, grid_coordinate: Tuple[int, int]) -> Tuple[int, int]:
        """
        Convert a grid position to a pixel one, using the cell size.
        """
        return grid_coordinate[0]*self.cell_size, grid_coordinate[1]*self.cell_size

    def PixelToGrid(self, pixel_coordinate: Tuple[int, int]) -> Tuple[int, int]:
        """
        Convert a pixel position to a grid one, using the cell size.
        """
        return int(pixel_coordinate[0]//self.cell_size), int(pixel_coordinate[1]//self.cell_size)

    def CreatePath(self, start_grid_coordinate: Tuple[int, int], end_grid_coordinate: Tuple[int, int], collision_rects_size=4) -> Tuple[List[Tuple[int, int]], List[pygame.Rect]]:
        """
        Create a new path between two grid positions.
        """
        start = self.grid.node(
            start_grid_coordinate[0], start_grid_coordinate[1])
        end = self.grid.node(end_grid_coordinate[0], end_grid_coordinate[1])
        self.current_path, _ = self.finder.find_path(start, end, self.grid)
        self.grid.cleanup()
        self.CreatePathCollisionRects(collision_rects_size)
        return self.current_path, self.collision_rects
