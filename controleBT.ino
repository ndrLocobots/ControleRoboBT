#include <SoftwareSerial.h>

// Define os pinos para o Bluetooth
#define BT_RX 6  // Pino que vai no TX do HC-05
#define BT_TX 7  // Pino que vai no RX do HC-05 (use divisor de tensão aqui)

SoftwareSerial bluetooth(BT_RX, BT_TX);  // RX, TX

// Pinos da ponte H
const int IN1 = 2;
const int IN2 = 3;
const int IN3 = 4;
const int IN4 = 5;

char comando = 'S';

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  bluetooth.begin(9600);  // Comunicação com o HC-05
  Serial.begin(9600);     // Opcional: para depuração no monitor serial
}

void loop() {
  if (bluetooth.available()) {
    comando = bluetooth.read();
    comando = toupper(comando);  // Garante letras maiúsculas
    Serial.println(comando);     // Só para teste/debug
  }

  switch (comando) {
    case 'F':
      frente();
      break;
    case 'B':
      tras();
      break;
    case 'L':
      esquerda();
      break;
    case 'R':
      direita();
      break;
    case 'S':
    default:
      parar();
      break;
  }
}

void frente() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void tras() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void esquerda() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void direita() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void parar() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
