# 🤖 AI Agent con Modelos Locales

Un agente de investigación inteligente que utiliza **modelos de lenguaje locales** (Ollama) para realizar búsquedas y responder preguntas de manera autónoma.

## 📋 Descripción

Este proyecto implementa un agente de IA que puede buscar información en la web y Wikipedia utilizando LangChain y modelos locales ejecutados con Ollama. El agente decide automáticamente qué herramientas usar según la consulta del usuario.

## ✨ Características

- 🏠 **100% Local**: Utiliza modelos de lenguaje ejecutados localmente con Ollama
- 🔍 **Búsqueda Web**: Integración con DuckDuckGo para búsquedas en internet
- 📚 **Wikipedia**: Acceso a información detallada de Wikipedia
- 🤖 **Agente Autónomo**: Decide qué herramientas usar según el contexto
- 🔒 **Privacidad**: Tus datos no salen de tu máquina

## 🛠️ Funciones Principales

### `main.py`

#### `check_ollama()`
Verifica que el servidor de Ollama esté ejecutándose antes de iniciar el agente. Realiza una petición HTTP a `localhost:11434` para confirmar la disponibilidad del servicio.

#### `main()`
Función principal que:
1. Verifica la conexión con Ollama
2. Inicializa el modelo local (Mistral)
3. Crea el agente con las herramientas disponibles
4. Procesa la consulta del usuario
5. Retorna la respuesta generada

### `tools.py`

#### `search_web(query: str)`
Herramienta que permite al agente buscar información en internet usando DuckDuckGo. Retorna resultados relevantes basados en la consulta.

#### `search_wikipedia(query: str)`
Herramienta que busca información detallada en Wikipedia. Ideal para obtener datos enciclopédicos y contexto histórico.

## 📦 Instalación

### 1. Instalar Ollama

#### Windows
1. Descarga el instalador desde [ollama.com/download](https://ollama.com/download)
2. Ejecuta el instalador `.exe`
3. Ollama se iniciará automáticamente como servicio

#### macOS
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Descargar el Modelo

Una vez instalado Ollama, descarga el modelo Mistral:

```bash
ollama pull mistral
```

Otros modelos disponibles:
- `ollama pull llama2` - Llama 2 (7B)
- `ollama pull codellama` - Code Llama (especializado en código)
- `ollama pull phi` - Phi-2 (más ligero)

### 3. Verificar que Ollama está corriendo

```bash
ollama serve
```

O verifica con:
```bash
curl http://localhost:11434/api/tags
```

### 4. Instalar uv (Gestor de Paquetes)

Este proyecto utiliza **uv**, un gestor de paquetes de Python ultrarrápido.

#### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Más información en: [docs.astral.sh/uv](https://docs.astral.sh/uv/)

### 5. Instalar Dependencias del Proyecto

Con uv instalado, sincroniza las dependencias del proyecto:

```bash
uv sync
```

Esto instalará automáticamente todas las dependencias definidas en `pyproject.toml`:
- langchain
- langchain-ollama
- langchain-community
- pydantic
- wikipedia
- gpt4all
- python-dotenv

## 🚀 Uso

1. Asegúrate de que Ollama esté corriendo:
```bash
ollama serve
```

2. Ejecuta el agente:
```bash
python main.py
```

3. Ingresa tu consulta cuando se te solicite:
```
¿En que se le puede ayudar? ¿Cuál es la capital de Francia?
```

## 📝 Ejemplo de Uso

```
✅ Ollama is running
¿En que se le puede ayudar? ¿Quién fue Albert Einstein?
Running agent...
Respuesta Limpia: Albert Einstein fue un físico teórico alemán...
```

## 🔧 Configuración

Puedes cambiar el modelo en `main.py`:

```python
llm = ChatOllama(
    model="mistral",  # Cambia a "llama2", "phi", etc.
    timeout=120  
)
```

## 📚 Tecnologías

- **Python**: Lenguaje de programación utilizado para desarrollar el proyecto
- **UV**: Gestor e instalador de paquetes de python
- **LangChain**: Framework para aplicaciones con LLMs
- **Ollama**: Ejecución local de modelos de lenguaje
- **DuckDuckGo**: Motor de búsqueda web
- **Wikipedia API**: Acceso a contenido enciclopédico

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**Nota**: Este proyecto requiere que Ollama esté instalado y corriendo localmente. No se conecta a APIs externas de modelos de lenguaje.
