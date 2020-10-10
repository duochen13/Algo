import java.util.*;


class Car {
    int type;
    int id;

    Car(int type, int id) {
        this.type = type;
        this.id = id;
    }

    public int getId() {
        return this.id;
    }
}

// Parking [1,2,2], arrival(small), depature(small, 3)
class ParkingLot {

    int[] parkingLots = new int[3];
    Map<Integer, Car> cars = new HashMap<>();
    int capacity;
    int size;

    ParkingLot(int[] parkingLots) {
        for (int i = 0; i < parkingLots.length; ++i) {
            this.parkingLots[i] = parkingLots[i];
        }
        this.capacity = 0;
        this.size = 0;
    }

    public void arrival(int type) {
        // error handling: invalid type
        if (type != 0 && type != 1 && type != 2)
            throw Exception("ERROR: Invalid car type.");
        // if there are avialable spots
        if (this.parkingLots[type] > 0) {
            // decrement number of parking lots
            this.parkingLots[type] -= 1;
            // add cars
            int id = this.size;
            this.cars.put(id, new Car(type, id));
            // increment capacity
            this.size++;
        // no spots
        } else {
            throw Exception("ERROR: No spots.");
        }
    }

    public void depature(int type, int id) {
        // error handling: invalid type
        if (type != 0 && type != 1 && type != 2)
            throw Exception("ERROR: Invalid car type.");
        // error handling: order out of capacity
        if (!this.cars.containsKey(id) || this.parkingLots[type] == 0) {
            throw Exception("ERROR: Invalid id.");
        }
        // remoce the car
        Car removedCar = this.cars.get(id);
        this.cars.remove(id);
        // decrement capacity
        this.parkingLots[type]--;
    }

}



class Solution {

    public static void main(String[] args) {
        System.out.println("args");
    }
}