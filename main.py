#!/usr/bin/python
import cv2
import numpy as np
import math

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Agent:
    def __init__(self, position, step_size, n_points):
        self.__position = position
        self.__step_size = step_size
        self.__n_points = n_points

    def draw_agent(self, image):
        cv2.circle(image, (self.__position.x, self.__position.y), 3, (255,0,0), -1) # Agent Draw

    def generate_points_lists(self):
        new_points_list = []
        inc_angle = (math.pi * 2)/self.__n_points
        angle = 0
        for i in range(self.__n_points):
            new_x = self.__step_size * math.cos(angle) + self.__position.x
            new_y = self.__step_size * math.sin(angle) + self.__position.y
            new_points_list.append((int(new_x), int(new_y)))

            angle += inc_angle

        return new_points_list
    
    def set_next_pos(self, position):
        self.__position = position
        

class Obstacle:
    def __init__(self, position, mu, sigma):
        self.__position = position
        self.__mu = mu
        self.__sigma = sigma
    
    def draw_obstacle(self, image):
        cv2.circle(image, (self.__position.x, self.__position.y), 3, (0,0,255), -1) # Draw Obstacle


    

class Goal:
    def __init__(self, position, mu, sigma):
        self.__position = position
        self.__mu = mu
        self.__sigma = sigma

    def draw_goal(self,image):
        cv2.circle(image, (self.__position.x, self.__position.y), 3, (0,255,0), -1) # Draw Goal location




if __name__ == "__main__":
    image = np.ones((480,640,3), dtype=np.uint8) * 255 # Empty numpy image array

    agent = Agent(Position(100, 100), 50, 10) # Agent Make
    agent.draw_agent(image)
    goal_location=Goal(Position(588,284),1,1)
    goal_location.draw_goal(image)

    points_to_plot = agent.generate_points_lists() # Agent generate points
    for point in points_to_plot:
        cv2.circle(image, point, 3, (255,0,255), -1)

    agent.set_next_pos(Position(points_to_plot[0][0], points_to_plot[0][1]))
    agent.draw_agent(image)

    points_to_plot = agent.generate_points_lists() # Agent generate points
    for point in points_to_plot:
        cv2.circle(image, point, 3, (255,0,255), -1)

    Obstacles = [Obstacle(Position(200,150), 1, 1), 
                 Obstacle(Position(350,200), 1, 1), 
                 Obstacle(Position(400,400), 1, 1)]

    for obstacle in Obstacles:
        obstacle.draw_obstacle(image)

    cv2.imshow('image', image)
    cv2.waitKey(0)
