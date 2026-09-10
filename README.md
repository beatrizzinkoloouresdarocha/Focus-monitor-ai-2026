# Focus Monitor - Inteligência Artificial para Produtividade

O **Focus Monitor** é uma aplicação em Python baseada em visão computacional que analisa em tempo real o nível de foco do usuário através da webcam, identificando momentos de distração, má postura ou ausência da tela.

## 🎯 Funcionalidades
* **Status Focado (Verde):** Identifica quando o usuário está olhando diretamente para a tela.
* **Status Distraído (Laranja):** Detecta quando o usuário desvia o olhar para os lados ou para baixo (ex: olhando o celular) e inicia a contagem do tempo inativo.
* **Status Ausente (Vermelho):** Notifica quando o usuário não está visível na câmera.

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **OpenCV** (Captura e processamento de vídeo)
* **MediaPipe** (Detecção e mapeamento facial com FaceMesh)
* **NumPy** (Cálculos vetoriais de orientação)

## ⚙️ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/beatrizzinkoloouresdarocha/Focus-monitor-ai-2026.git](https://github.com/beatrizzinkoloouresdarocha/Focus-monitor-ai-2026.git)
   cd Focus-monitor-ai-2026