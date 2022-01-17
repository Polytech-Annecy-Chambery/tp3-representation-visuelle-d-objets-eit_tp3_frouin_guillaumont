# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl
from Section import Section

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0
            
        # Generates the opening from parameters
        self.generate()  
        
        self.objects = []

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [ 
                [0,0,0], 
                [0, 0, self.parameters['height']],
                [0, self.parameters['thickness'], self.parameters['height']],
                [0, self.parameters['thickness'], 0],
                [self.parameters['width'], 0 , 0 ],
                [self.parameters['width'], 0 , self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], 0]
                ]
        self.faces = [
                [0,1,2,3],
                [4,5,6,7],
                [0,3,7,4],
                [1,2,6,5]
                ]   
        
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        for i in self.faces:
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv([self.parameters['color'][0]*0.5,self.parameters['color'][1]*0.5,self.parameters['color'][2]*0.5])
            for j in i:
                gl.glVertex3fv(self.vertices[j])
            gl.glEnd()
        gl.glPopMatrix() 
        
    # Draws the faces                
    def draw(self):        
        # A compléter en remplaçant pass par votre code
        self.drawEdges()
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        for i in self.faces :
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv(self.parameters['color']) # Couleur gris moyen
            for j in i :
                gl.glVertex3fv(self.vertices[j])
            gl.glEnd()
        gl.glPopMatrix()  