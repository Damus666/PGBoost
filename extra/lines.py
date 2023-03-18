import sys
#sys.path.append("...")
from ..extra.math import Math
from typing import Tuple, Union
import pygame
import math


"""
Contains the Segment and Line class.
"""


class Segment():
    """
    A useful class to more easly work with segments in pygame or in general.
    """

    def __init__(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int], color: Union[str, Tuple[int, int, int],pygame.Color] = "white", thicness: int = 2):
        self.start:pygame.Vector2 = pygame.math.Vector2(start_pos)
        """The start point. <get, set>"""
        self.end:pygame.Vector2 = pygame.math.Vector2(end_pos)
        """The end point. <get, set>"""
        self.color:str|tuple[int,int,int]|pygame.Color = color
        """The color. <get, set>"""
        self.thicness:int = thicness
        """The thicness. <get, set>"""

    def ToTuple(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """Returns a tuple representation of the segment."""
        return (self.start.xy, self.end.xy)

    def CollideRect(self, rect: pygame.Rect) -> bool:
        """Checks if the segment intersects a rect."""
        return any([self.TupleIntersects((rect.topleft, rect.bottomleft)), self.TupleIntersects((rect.topleft, rect.topright)), self.TupleIntersects((rect.bottomleft, rect.bottomright)), self.TupleIntersects((rect.topright, rect.bottomright))])

    def SetStart(self, pos: Tuple[int, int]):
        """
        Sets the start xy attribute.
        """
        self.start.xy = (pos[0], pos[1])

    def SetEnd(self, pos: Tuple[int, int]):
        """
        Sets the end xy attribute.
        """
        self.end.xy = (pos[0], pos[1])

    def Int(self):
        """
        Corrects any non-int value on the points.
        """
        self.start.x = int(self.start.x)
        self.start.y = int(self.start.y)
        self.end.x = int(self.end.x)
        self.end.y = int(self.end.y)

    def IntPoint(self, point: Tuple[float, float]) -> Tuple[int, int]:
        """
        Corrects any non-int values in a point and return it.
        """
        return (int(point[0]), int(point[1]))

    def Move(self, x: int, y: int):
        """
        Moves the segment by an amount.
        """
        self.start.x += x
        self.start.y += y
        self.end.x += x
        self.end.y += y

    def Extend(self, amount:int, extend_start:bool=False)->tuple[float,float]:
        """Changes the segment size."""
        current_x = self.end.x-self.start.x
        current_y = self.end.y-self.start.y
        if current_x == 0:
            if extend_start:
                self.start.y += amount
            else:
                self.end.y += amount
            return 0, amount
        if current_y == 0:
            if extend_start:
                self.start.x += amount
            else:
                self.end.x += amount
            return amount, 0
        hypotenus = math.sqrt((current_x**2+current_y**2))
        hypotenus += amount
        new_x = math.sqrt((hypotenus**2-current_y**2))
        new_y = math.sqrt((hypotenus**2-current_x**2))
        offset_x = new_x-current_x
        offset_y = new_y-current_y
        if extend_start:
            self.start.y += offset_y
            self.start.x += offset_x
        else:
            self.end.y += offset_y
            self.end.x += offset_x
        return offset_x, offset_y

    def Copy(self):
        """
        Returns an exact copy of the segment.
        """
        return Segment(self.start, self.end, self.color, self.thicness)

    def ToLine(self):
        """
        Returns a line with the same properties of this segment.
        """
        return Line(self.start, self.end, self.color, self.thicness)

    def Lenght(self) -> float:
        """
        Returns the lenght of the segment.
        """
        return math.dist(self.start, self.end)

    def Slope(self) -> float:
        """
        Returns the slope of the segment.
        """
        if (self.end.x-self.start.x) == 0:
            return None
        return (self.end.y-self.start.y)/(self.end.x-self.start.x)

    def IsParallel(self, segment) -> bool:
        """
        Checks if two segments are parallel.
        """
        return self.Slope() == segment.Slope()

    def TupleIsParallel(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> bool:
        """
        Checks if this segment and a tuple based segment are parallel.
        """
        return self.Slope() == Math.TupleSlope(tuplee)

    def TupleIntersectionPoint(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> Tuple[float, float]:
        """
        If the segment and the tuple based segment intersects, return the point, otherwise return (None,None)
        """
        if not self.TupleIsParallel(tuplee):
            if self.TupleIntersects(tuplee):
                return self.TupleAbsoluteIntersectionPoint(tuplee)
        return (None, None)

    def TupleAbsoluteIntersectionPoint(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> Tuple[float, float]:
        """
        Calculates the intersection point of a segment and a tuple based segment (non parallel) even if the point is not inside them.
        """
        if self.TupleIsParallel(tuplee):
            raise ValueError("Parallel segments cannot intersect.")

        xdiff = (self.start.x-self.end.x, tuplee[0][0]-tuplee[1][0])
        ydiff = (self.start.y-self.end.y, tuplee[0][1]-tuplee[1][1])

        div = Math.Det(xdiff, ydiff)

        d = (Math.Det(self.start, self.end), Math.Det(tuplee[0], tuplee[1]))
        return (Math.Det(d, xdiff)/div, Math.Det(d, ydiff)/div)

    def TupleIntersects(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> bool:
        """
        Checks if the segment and a tuple based segment intersects.
        """
        if not self.TupleIsParallel(tuplee):
            point = self.TupleAbsoluteIntersectionPoint(tuplee)
            return Math.InsideEqualRange(self.start.x, self.end.x, point[0]) and Math.InsideEqualRange(tuplee[0][0], tuplee[1][0], point[0]) and Math.InsideEqualRange(self.start.y, self.end.y, point[1]) and Math.InsideEqualRange(tuplee[0][1], tuplee[1][1], point[1])
        return False

    def AbsoluteIntersectionPoint(self, segment) -> Tuple[float, float]:
        """
        Calculates the intersection point of two segments (non parallel) even if the point is not inside them.
        """
        if self.IsParallel(segment):
            raise ValueError("Parallel segments cannot intersect.")

        xdiff = (self.start.x-self.end.x, segment.start.x-segment.end.x)
        ydiff = (self.start.y-self.end.y, segment.start.y-segment.end.y)

        div = Math.Det(xdiff, ydiff)
        if div == 0:
            div = 0.0000001

        d = (Math.Det(self.start, self.end), Math.Det(segment.start, segment.end))
        return (Math.Det(d, xdiff)/div, Math.Det(d, ydiff)/div)

    def IntersectionPoint(self, segment) -> Tuple[float, float]:
        """
        If the segments intersects, return the point, otherwise return (None,None)
        """
        if not self.IsParallel(segment):
            if self.Intersects(segment):
                return self.AbsoluteIntersectionPoint(segment)
        return (None, None)

    def Intersects(self, segment) -> bool:
        """
        Checks if the segments intersects.
        """
        if not self.IsParallel(segment):
            point = self.AbsoluteIntersectionPoint(segment)
            return Math.InsideEqualRange(self.start.x, self.end.x, point[0]) and Math.InsideEqualRange(segment.start.x, segment.end.x, point[0]) and Math.InsideEqualRange(self.start.y, self.end.y, point[1]) and Math.InsideEqualRange(segment.start.y, segment.end.y, point[1])
        return False

    def Draw(self, surface: pygame.Surface):
        """
        Draws the segment.
        """
        pygame.draw.line(surface, self.color, self.start.xy,
                         self.end.xy, width=self.thicness)


class Line():
    """
    Similar to the segment, but with slightly different math, as two non parallel lines always have an intersection.
    """

    def __init__(self, point1: Tuple[int, int], point2: Tuple[int, int], color: Union[str, Tuple[int, int], pygame.Color] = "white", thicness: int = 2):
        self.point1:pygame.Vector2 = pygame.math.Vector2(point1)
        """One of the 2 points. <get, set>"""
        self.point2:pygame.Vector2 = pygame.math.Vector2(point2)
        """One of the 2 points. <get, set>"""
        self.color:str|tuple[int,int,int]|pygame.Color = color
        """The color. <get, set>"""
        self.thicness:int = thicness
        """The thicness. <get, set>"""

    def ToTuple(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        return (self.point1.xy, self.point2.xy)

    def CollideRect(self, rect: pygame.Rect) -> bool:
        return any([self.TupleIntersects((rect.topleft, rect.bottomleft)), self.TupleIntersects((rect.topleft, rect.topright)), self.TupleIntersects((rect.bottomleft, rect.bottomright)), self.TupleIntersects((rect.topright, rect.bottomright))])

    def SetPoint1(self, pos: Tuple[int, int]):
        """
        Sets the point1 xy attribute.
        """
        self.point1.xy = (pos[0], pos[1])

    def SetPoint2(self, pos: Tuple[int, int]):
        """
        Sets the point2 xy attribute.
        """
        self.point2.xy = (pos[0], pos[1])

    def Int(self):
        """
        Corrects any non-int value on the points.
        """
        self.point1.x = int(self.point1.x)
        self.point1.y = int(self.point1.y)
        self.point2.x = int(self.point2.x)
        self.point2.y = int(self.point2.y)

    def IntPoint(self, point: Tuple[float, float]) -> Tuple[int, int]:
        """
        Corrects any non-int values in a point and return it.
        """
        return (int(point[0]), int(point[1]))

    def Move(self, x: int, y: int):
        """
        Moves the line by an amount.
        """
        self.point1.x += x
        self.point1.y += y
        self.point2.x += x
        self.point2.y += y

    def Length(self) -> float:
        """
        Returns the lenght between the two known points.
        """
        return math.dist(self.point1, self.point2)

    def Slope(self) -> float:
        """
        Returns the slope of the line.
        """
        if (self.point2.x-self.point1.x) == 0:
            return None
        return (self.point2.y-self.point1.y)/(self.point2.x-self.point1.x)

    def IsParallel(self, line) -> bool:
        """
        Checks if two lines are parallel.
        """
        return self.Slope() == line.Slope()

    def TupleIsParallel(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> bool:
        """
        Checks if this line and a tuple based line are parallel.
        """
        return self.slope() == Math.TupleSlope(tuplee)

    def tuple_intersection_point(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> Tuple[float, float]:
        """
        If the line and the tuple based line intersects, return the point, otherwise return (None,None)
        """
        if not self.TupleIsParallel(tuplee):
            return self.TupleAbsoluteIntersectionPoint(tuplee)
        return (None, None)

    def TupleAbsoluteIntersectionPoint(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> Tuple[float, float]:
        """
        Calculates the intersection point of a line and a tuple based line (non parallel) even if the point is not inside them.
        """
        if self.TupleIsParallel(tuplee):
            raise ValueError("Parallel lines cannot intersect.")

        xdiff = (self.point1.x-self.point2.x, tuplee[0][0]-tuplee[1][0])
        ydiff = (self.point1.y-self.point2.y, tuplee[0][1]-tuplee[1][1])

        div = Math.Det(xdiff, ydiff)

        d = (Math.Det(self.point1, self.point2), Math.Det(tuplee[0], tuplee[1]))
        return (Math.Det(d, xdiff)/div, Math.Det(d, ydiff)/div)

    def TupleIntersects(self, tuplee: Tuple[Tuple[float, float], Tuple[float, float]]) -> bool:
        """
        Checks if the segment and a tuple based segment intersects.
        """
        if not self.TupleIsParallel(tuplee):
            return True
        return False

    def Copy(self):
        """
        Returns an exact copy of the line.
        """
        return Line(self.point1, self.point2, self.color, self.thicness)

    def ToSegment(self):
        """
        Converts the line to a segment.
        """
        return Segment(self.point1, self.point2, self.color, self.thicness)

    def AbsoluteIntersectionPoint(self, line) -> Tuple[float, float]:
        """
        Calculates the intersection point of two lines (non parallel, otherwise throws an error).
        """
        if self.IsParallel(line):
            raise ValueError("Parallel lines cannot intersect.")

        xdiff = (self.point1.x-self.point2.x, line.point1.x-line.point2.x)
        ydiff = (self.point1.y-self.point2.y, line.point1.y-line.point2.y)

        div = Math.Det(xdiff, ydiff)

        d = (Math.Det(self.point1, self.point2), Math.Det(line.point1, line.point2))
        return (Math.Det(d, xdiff)/div, Math.Det(d, ydiff)/div)

    def IntersectionPoint(self, line) -> Tuple[float, float]:
        """
        If the lines are not parallel, return the intersection point, otherwise return (None,None)
        """
        if not self.IsParallel(line):
            return self.AbsoluteIntersectionPoint(line)
        return (None, None)

    def Intersects(self, line) -> bool:
        """
        Checks if the lines intersects (aka if they are not parallel).
        """
        if not self.IsParallel(line):
            return True
        return False

    def Draw(self, surface: pygame.Surface):
        """
        Draws the line (it will look like a segment).
        """
        pygame.draw.line(surface, self.color, self.point1.xy,
                         self.point2.xy, width=self.thicness)
