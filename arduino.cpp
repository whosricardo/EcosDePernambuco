// Configuração dos LDRs e variáveis
const int ldrPins[8] = {A0, A1, A2, A3, A4, A5, A6, A7}; // Pinos analógicos dos LDRs
const int threshold = 500; // Limite de leitura do LDR para detectar luz
int previousState[8] = {0, 0, 0, 0, 0, 0, 0, 0}; // Estado anterior dos LDRs

void setup() {
    Serial.begin(9600); // Inicializa a comunicação serial
    for (int i = 0; i < 8; i++) {
        pinMode(ldrPins[i], INPUT); // Define os pinos dos LDRs como entrada
    }
}

void loop() {
    for (int i = 0; i < 8; i++) {
        int ldrValue = analogRead(ldrPins[i]); // Lê o valor do LDR

        // Detecta mudança de estado (luz detectada)
        if (ldrValue > threshold && previousState[i] == 0) {
            Serial.print("AUDIO_");
            Serial.println(i + 1); // Envia o comando "AUDIO_1", "AUDIO_2", etc.
            previousState[i] = 1; // Atualiza o estado para evitar repetições
        } 
        // Detecta ausência de luz e reseta o estado
        else if (ldrValue <= threshold && previousState[i] == 1) {
            previousState[i] = 0;
        }
    }
    
    delay(100); // Evita leituras muito rápidas
}
