def checkOverlap(
    self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int
) -> bool:
    nearest_x = max(x1, min(xCenter, x2))
    nearest_y = max(y1, min(yCenter, y2))
    distance_x = nearest_x - xCenter
    distance_y = nearest_y - yCenter
    return distance_x**2 + distance_y**2 <= radius
