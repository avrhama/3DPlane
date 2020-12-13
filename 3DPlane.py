import pygame,random,sys,math
from math import sin,cos,radians

DisplayWidth=300
DisplayHeight=300
clock = pygame.time.Clock()
pygame.init()
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
def subs(p1,p2):
	return (p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])
def add(p1,p2):
	return (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2])
def rotateZ_point(pivot,teta,p):
	teta=radians(teta)
	s=sin(teta)
	c=cos(teta)
	p=subs(p,pivot)
	p=(p[0]*c-p[1]*s,p[0]*s+p[1]*c,p[2])
	return add(p,pivot)

def rotateX_point(pivot,teta,p):
	teta=radians(teta)
	s=sin(teta)
	c=cos(teta)
	p=subs(p,pivot)
	p=(p[0],p[1]*c-p[2]*s,p[1]*s+p[2]*c)
	return add(p,pivot)

def rotateY_point(pivot,teta,p):
	teta=radians(teta)
	s=sin(teta)
	c=cos(teta)
	p=subs(p,pivot)
	p=(p[0]*c-p[2]*s,p[1],p[0]*s+p[2]*c)
	return add(p,pivot)

offsetX=60
offsetY=60
p1=(55+offsetX,10+offsetY,0)
p2=(10+offsetX,160+offsetY,0)
p3=(40+offsetX,160+offsetY,0)
p4=(55+offsetX,160+offsetY,30)
p5=(70+offsetX,160+offsetY,0)
p6=(100+offsetX,160+offsetY,0)
points=[p1,p2,p3,p4,p5,p6]
pivot=(50+offsetX,85+offsetY,15)
teta=10
while True:
	gameDisplay.fill((0,255,255))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_q:
				for i in range(len(points)):
					points[i]=rotateZ_point(pivot,teta,points[i])
					
			if event.key==pygame.K_w:
				for i in range(len(points)):
					points[i]=rotateZ_point(pivot,-teta,points[i])
			if event.key==pygame.K_a:
				for i in range(len(points)):
					points[i]=rotateX_point(pivot,teta,points[i])
			if event.key==pygame.K_s:
				for i in range(len(points)):
					points[i]=rotateX_point(pivot,-teta,points[i])
			if event.key==pygame.K_z:
				for i in range(len(points)):
					points[i]=rotateY_point(pivot,teta,points[i])
			if event.key==pygame.K_x:
				for i in range(len(points)):
					points[i]=rotateY_point(pivot,-teta,points[i])
	if True:#change to False if you want to control the rotation
		for i in range(len(points)):
			points[i]=rotateX_point(pivot,teta,points[i])
		for i in range(len(points)):
			points[i]=rotateY_point(pivot,teta,points[i])
		for i in range(len(points)):
			points[i]=rotateZ_point(pivot,teta,points[i])
	
	pygame.draw.line(gameDisplay,(255,255,255),(points[0][0],points[0][1]),(points[1][0],points[1][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[0][0],points[0][1]),(points[2][0],points[2][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[0][0],points[0][1]),(points[3][0],points[3][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[0][0],points[0][1]),(points[4][0],points[4][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[0][0],points[0][1]),(points[5][0],points[5][1]),1)

	pygame.draw.line(gameDisplay,(255,255,255),(points[1][0],points[1][1]),(points[2][0],points[2][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[2][0],points[2][1]),(points[3][0],points[3][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[3][0],points[3][1]),(points[4][0],points[4][1]),1)
	pygame.draw.line(gameDisplay,(255,255,255),(points[4][0],points[4][1]),(points[5][0],points[5][1]),1)
	
	pygame.display.update()
	clock.tick(5)
	