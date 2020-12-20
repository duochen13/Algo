#include <iostream>
#include <string>

template <typename F, typename T>
void callFunc(F f, T t) {
    f(t);
}

template <typename F, typename T, typename A>
void callFunc(F f, T t, A a) {
    f(t, a);
}

void hoo(int t) {
    std::cout << "hoo(int t) template called with: " << t << std::endl;
}

void hoo(std::string t) {
    std::cout << "hoo(string t) template called with: " << t << std::endl;
}

void goo(int t) {
    std::cout << "goo(int t) template called with: " << t << std::endl;
}

void goo(int t, double a) {
    std::cout << "goo(int t, double a )template called with: " << t << " and " << std::endl;
}


void greetings(std::string name) { std::cout << "Hello! " << name << std::endl; }
void screaming(int level) { std::cout << "My panic level is " << level << std::endl; }

int main(int argv, char **argc) {
    
    std::string name = "Duo";
    int level = -10;
    callFunc(greetings, name);
    callFunc(screaming, level);

    // not working:  callFunc(hoo<int, std::string>, level);  
    callFunc(static_cast<void (*)(int)>(hoo), level);
    callFunc(static_cast<void (*)(std::string)>(hoo), name);
    callFunc<void (*)(int)>(hoo, level);
    callFunc<void (*)(std::string)>(hoo, name);
    callFunc<void (*)(int)>(goo, level);
    callFunc<void (*)(int t, double a)>(goo, level, 1.2);
    return 0;
}
