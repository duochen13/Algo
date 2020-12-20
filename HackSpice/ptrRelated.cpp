#include <iostream>

class DummySheep {
    int age;
    public:
        DummySheep(int age_);
        void printAge();
};


DummySheep::DummySheep(int age_) {
    age = age_;
}

void DummySheep::printAge() {
    std::cout << "age: " << age << std::endl;
}

int main(int argc, char** argv) {

    DummySheep sheep1 = DummySheep(10);
    sheep1.printAge(); // 10

    int *evilPtr = (int *)(&sheep1);
    // modify private var
    *evilPtr *= 10;

    sheep1.printAge(); // 100

    return 0;
}
