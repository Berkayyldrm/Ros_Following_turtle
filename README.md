# Ros_Following_turtle
One turtle follows other turtle in Ros Turtlesim

# ENG

# Two robots were used in this project in Ros turtlesim.

# The state vector of robots is denoted by [x, y, θ].T
   X and y are position of robots in 2D; θ is the heading angle.
   Robot-1 will spawn in [0,0,0].T, Robot-2 will spawn in a randomly determined situation, provided it is in the working space
    
# Motion Controller(ROS node) will be written for each one robot.
   • Robot-1's motion controller is designed to follow Robot-2 from a specified distance. Robot-1 can access state info of Robot-2
    
   • Robot-2's motion controller is designed according to the following motion strategy.
       o Robot-2 moves with current heading angle and determined constant speed. 
       o When Robot-2 reaches working space limits, its acts like reflection of light from the mirror. So the angle that the heading of arrival makes with the normal is equal to          the angle that the heading of rotation makes with the normal.
     
   • Linear and angular maximum velocities and tracking distance of the robots were read parametrically from the JSON file at the beginning.


# TR

# Projede ROS turtlesim ortamında iki adet robot kullanılmıştır.

# Robotların durum vektörü [x, y, θ].T ile gösterilmektedir.
   Burada x ve y, robotun 2B ortamdaki  pozisyonunu; θ ise doğrultu açısını göstermektedir.
   Robot-1, [0,0,0].T; Robot-2 ise çalışma ortamında olmak kaydıyla random olarak belirlenmiş bir durumda başlayacaktır.

# Her bir robot için hareket-kontrolcüsü (ROS node) yazılacaktır.
  • Robot-1’in hareket kontrolcüsü, Robot-2’yi belirlenen mesafeden takip edecek şekilde
  tasarlanmıştır. Robot-1, Robot-2’nin durum bilgisine ulaşabilmektedir.

  • Robot-2’nin hareket kontrolcüsü, aşağıdaki hareket stratejisine göre tasarlanmıştır:
      o Robot-2 mevcut doğrultu açısında ve belirlenmiş sabit hızda hareket eder.
      o Robot-2 çalışma ortamı sınırına geldiğinde, ışığın aynadan yansıması gibi hareket eder. Yani geliş
        doğrultusunun normalle yaptığı açı, dönüş yönünün normalle yaptığı açıya eşittir.
  
  • Robotların (linear ve angular) maks. hızları ve takip mesafesi parametrik olarak, başlangıçta JSON
    dosyasından okunmuştur.

