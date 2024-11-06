#ifdef MATH_DYNAMIC_H
#define MATH_DYNAMIC_H
#include <math.h>
// fast actions dentro do codigo!
inline int fast_add(int a,int b) {
  return a + b;
}
inline int fast_sub(int a,int b) {
  return a - b;
}
inline int fast_mul(int a,int b) {
  return a * b;
}
// Fucoes rapidas do math!
inline float fast_sqrt(float x) {
  return sqrtf(x);
}
inline float fast_sin(float x) {
  return sinf(x);
}
#endif // fim
