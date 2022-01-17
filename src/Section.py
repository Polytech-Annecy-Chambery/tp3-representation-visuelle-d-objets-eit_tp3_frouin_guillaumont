# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
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
                [0,0,self.parameters['height']],
                [self.parameters['width'],0,self.parameters['height']],
                [self.parameters['width'],0,0],
                [0,self.parameters['thickness'],0],
                [0,self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],0]
                ]
        
        self.faces = [
                [0,3,2,1],
                [4,7,6,5],
                [0,4,5,1],
                [3,7,6,2],
                [0,4,7,3],
                [1,5,6,2]
                ]    

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        if x.parameters['thickness'] == self.parameters['thickness'] :
          if x.parameters['position'][0] >= self.parameters['position'][0] :
            if x.parameters['position'][1] >= self.parameters['position'][1] :
              if x.parameters['position'][2] >= self.parameters['position'][2] :
                if x.parameters['position'][2] + x.parameters['height'] <= self.parameters['position'][2] + self.parameters['height']:
                  if x.parameters['position'][0] + x.parameters['width'] <= self.parameters['position'][0] + self.parameters['width']:
                    return True 
        return False      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        if self.canCreateOpening(x) == True:
            section1 = Section({'position':self.parameters['position'], 
                     'width':x.parameters['position'][0],
                     'height':self.parameters['height'],
                     'thickness': self.parameters['thickness']})
            
            section2 = Section({'position':[x.parameters['position'][0],x.parameters['position'][1],x.parameters['position'][2]+x.parameters['height']],
                     'width':x.parameters['width'],
                     'height':self.parameters['height']-x.parameters['position'][2]-x.parameters['height'],
                     'thickness': self.parameters['thickness']})
            
            section3 = Section({'position':[x.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2]],
                     'width':x.parameters['width'],
                     'height':x.parameters['position'][2],
                     'thickness': x.parameters['thickness']})
            
            section4 = Section({'position':[x.parameters['position'][0]+x.parameters['width'],x.parameters['position'][1],self.parameters['position'][2]],
                     'width':self.parameters['width']-x.parameters['position'][0]-x.parameters['width'],
                     'height':self.parameters['height'],
                     'thickness': x.parameters['thickness']})
            
            return [section1,section2,section3,section4]
                      
        
    # Draws the edges
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
        if self.parameters['edges']:
            self.drawEdges()
        
        
        for face in self.faces:
            gl.glPushMatrix()
            gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
            gl.glRotate(self.parameters['orientation'],0,0,1)
        
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv([0.5, 0.5, 0.5])
            gl.glVertex3fv(self.vertices[face[0]])
            gl.glVertex3fv(self.vertices[face[1]])
            gl.glVertex3fv(self.vertices[face[2]])
            gl.glVertex3fv(self.vertices[face[3]])
            gl.glEnd()
            gl.glPopMatrix()
  