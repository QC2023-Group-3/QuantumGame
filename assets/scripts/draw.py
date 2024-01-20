import json
import pygame

# Open colors selection
with open('../style.json') as styles: COLORS = json.load(styles)['colors']

# Draw obstacles
def drawObstacle(surface, obstacles) -> None:
	for obstacle in obstacles:
		left = obstacle.beginX
		top = obstacle.beginY
		width = abs(obstacle.beginX-obstacle.beginY)
		height = abs(obstacle.beginY-obstacle.endY)

		pygame.draw.rect(surface, COLORS["obstacle"], pygame.Rect(left, top, width, height))

# Draw the ball
def drawBall(surface, ball, particleWidth) -> None:
	psi = ball.psi
	# Converting psi/matrix to a surface
	for y in psi:
		for x in y:
			currColor = int(x*255)
			color = [i*currColor for i in COLORS["ballHeatmap"]] # Select which RGB values should be colored

			pygame.draw.rect(surface, color, (x-(particleWidth/2), y-(particleWidth/2), particleWidth, particleWidth))