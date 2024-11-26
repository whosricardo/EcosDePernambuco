// Configuração dos LDRs e variáveis
const int ldrPins[2] = {A0, A1}; // Pinos analógicos dos LDRs das direções
const int langPins[3] = {A8, A9, A10}; // Pinos analógicos dos LDRs de idioma
const int threshold = 700; // Limite de leitura do LDR para detectar luz
int previousState[2] = {0, 0}; // Estado anterior dos LDRs de direção
int currentLang = -1; // Idioma atualmente selecionado (-1 = nenhum)

void setup() {
    Serial.begin(9600); // Inicializa a comunicação serial
    for (int i = 0; i < 2; i++) {
        pinMode(ldrPins[i], INPUT); // Define os pinos dos LDRs de direção como entrada
    }
    for (int i = 0; i < 3; i++) {
        pinMode(langPins[i], INPUT); // Define os pinos dos LDRs de idioma como entrada
    }
}

void loop() {
    // Detecta idioma (independente das direções)
    int detectedLang = -1; // Nenhum idioma detectado inicialmente
    int activeLangCount = 0; // Contador de idiomas ativos

    for (int i = 0; i < 3; i++) {
        int langValue = analogRead(langPins[i]); // Lê o valor do LDR de idioma
        if (langValue > threshold) {
            detectedLang = i; // Armazena o índice do idioma detectado
            activeLangCount++; // Incrementa o número de idiomas detectados
        }
    }

    // Atualiza o idioma apenas se um único idioma estiver ativo
    if (activeLangCount == 1 && detectedLang != currentLang) {
        currentLang = detectedLang; // Atualiza o idioma atual
        Serial.print("LANG_");
        Serial.println(currentLang); // Envia "LANG_0", "LANG_1", ou "LANG_2"
    }

    // Detecta direção (independente dos idiomas)
    for (int i = 0; i < 2; i++) {
        int ldrValue = analogRead(ldrPins[i]); // Lê o valor do LDR de direção
        if (ldrValue > threshold && previousState[i] == 0) {
            Serial.print("AUDIO_");
            Serial.println(i + 1); // Envia "AUDIO_1", "AUDIO_2", etc.
            previousState[i] = 1; // Atualiza o estado para evitar repetições
        } else if (ldrValue <= threshold && previousState[i] == 1) {
            previousState[i] = 0; // Reseta o estado se o LDR não estiver mais iluminado
        }
    }

    delay(100); // Evita leituras muito rápidas
}
