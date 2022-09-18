#include <GL/glut.h>

void init(void){
    // multiply the current matrix with an orthographic matrix
    // (left, right, bottom, top, nearVal, farVal)
    // (left, right) = Specify the coordinates for the vertical clipping
    // (bottom, top) = specify the coordinated for the horizontal clipping
    glOrtho (0.0, 200.0, 0.0, 150.0, -1.0, 1.0);
}

void lineSegment(void){
    // Clear display window
    glClear(GL_COLOR_BUFFER_BIT);

    // Set line color to green
    glColor3f(1, 1, 0);
    glBegin(GL_LINES);
    glVertex2i(180, 15);
    glVertex2i(10, 145);

    glEnd();
    glFlush();
}

int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Line drawing");

    init();
    glutDisplayFunc(lineSegment);
    glutMainLoop();

    return 0;
}
