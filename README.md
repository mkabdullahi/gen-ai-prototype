# Ollama Streamlit Interface

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit Version](https://img.shields.io/badge/streamlit-1.36.0-green)

A production-ready interface for interacting with Ollama language models with adjustable parameters and safety features.

## Features
- 🛡️ Input validation & sanitization
- ⏱️ Rate limiting (configurable via .env)
- ⏳ 30-second request timeout
- 🤖 Multiple model support (llama3, mistral, phi3)
- 📊 Response length controls
- 📈 Usage tracking
- 🔄 Automatic error recovery

## Installation
```bash
# Clone repository
git clone https://github.com/mkabdullahi/gen-ai-prototype
cd gen-ai-prototype

# Install dependencies
pip install -r requirements.txt

# Install Ollama models
ollama pull llama3
```

## Configuration
Create `.env` file:
```bash
# Ollama configuration
OLLAMA_HOST=http://localhost:11434  # API endpoint
MAX_REQUESTS_PER_MIN=5              # Rate limit
REQUEST_TIMEOUT=30                   # In seconds
```

## Deployment Checklist
1. Configure reverse proxy (Nginx/Apache)
2. Set up process manager (systemd/pm2)
3. Enable monitoring:
   ```bash
   journalctl -u ollama-service -f
   ```
4. Configure firewall rules
5. Set up automated backups

## Model Licenses
- **Llama 3**: [Meta AI License](https://llama.meta.com/llama3)
- **Mistral**: [Apache 2.0 License](https://mistral.ai/)
- **Phi-3**: [MIT License](https://microsoft.com/phi-3)

## Troubleshooting
```bash
# Check service status
systemctl status ollama

# View logs
journalctl -u ollama -n 50 -f
```

## Contributing
1. Fork the repository
2. Create feature branch
3. Submit PR with:
   - Updated tests
   - Documentation changes
   - Clear commit messages

![App Screenshot](/path/to/screenshot.png)
