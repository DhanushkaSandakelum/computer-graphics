#include <stdlib.h>
#include <math.h>
#include <GL/glu.h>
#include <GL/glut.h>

void init(void){
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // multiply the current matrix with an orthographic matrix
    // (left, right, bottom, top, nearVal, farVal)
    // (left, right) = Specify the coordinates for the vertical clipping
    // (bottom, top) = specify the coordinated for the horizontal clipping
    glOrtho (0.0, 500.0, 0.0, 500.0, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);

}

// Bresenham line drawing procedure for 0 < m < 1
void DrawBresenhamLine() {
    GLfloat x1=120, y1=50, x2=300, y2=350;
    GLfloat M, p, dx, dy, x, y;

    glClear(GL_COLOR_BUFFER_BIT);

    if((x2 - x1) == 0){
        M = (y2 - y1);
    } else {
        M = (y2 - y1)/(x2 - x1);
    }

    dx = x2 - x1;
    dy = y2 - y1;

    p = 2*dy - dx;

    x = x1;
    y = y1;

    glBegin(GL_POINTS);
        while(x <= x2){
            glVertex2f(x, y);
            x = x + 1;

            if(p >= 1){
                y = y + 1;
                p = p+ 2*dy - 2*dx;
            } else {
                y = y;
                p = p + 2*dy;
            }
        }
    glEnd();

    glFlush();
}

int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Bresenham Line drawing");

    init();
    glutDisplayFunc(DrawBresenhamLine);
    glutMainLoop();

    return 0;
}
