
#ifndef HOME_ICE
#define HOME_ICE

module generated
{
  
  exception NoInput {};
  exception InvalidArgument{string message;};
  dictionary <string, int> contents;

  interface Camera
  {
  void move(double phi, double psi);
  void zoomIn(double value);
  void zoomOut(double value);
  bool moveDetected();
  };
  interface CentralHeating
  {
  void turnOn();
  void turnOff();
  bool isOn();
  double getTemperature();
  void setTemperature(double temperature);
  };
  interface Fridge
  {
  void put(string product, int amount);
  void take(string product, int amount);
  contents list();
  void setTemperature(double temperature);
  };
  interface GardenCamera extends Camera{
  void turnInfraredOn();
  void turnInfraredOff();
  };
  interface Lamp{
  void turnOn();
  void turnOff();
  bool isOn();
  void setBrightness(int lumens);
  };
  interface Garage{
  void open();
  void close();
  bool isOpen();
  };
};

#endif
