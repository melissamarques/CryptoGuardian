# CryptoGuardian

CryptoGuardian é um pacote Python que fornece uma ferramenta simples e poderosa de criptografia e descriptografia de arquivos. Ele permite que você proteja seus arquivos confidenciais com criptografia forte usando a biblioteca de criptografia Fernet.

## Características

- **Criptografia de arquivo**: criptografe facilmente seus arquivos para proteger dados confidenciais.
- **Descriptografia de arquivo**: Descriptografe arquivos criptografados anteriormente quando precisar acessar seu conteúdo.
- **Gerenciamento de senhas**: gere automaticamente chaves de criptografia fortes e copie-as para a área de transferência para proteção.

### Instalação

Você pode instalar o CryptoGuardian via `pip`:

```
pip install cryptoguardian
```

### Uso

```
from cryptoguardian import CryptoGuardian
```

# Crie uma instância do CryptoGuardian

```
guardian = CryptoGuardian()
```

# Criptografar um arquivo

```
guardian.criptografar_arquivo()
```

Copie o caminho para o arquivo que deseja criptografar e cole no terminal **Ex.: C:\Users\Melissa\Desktop\ufpi/logo.png**

Copie a senha que foi gerada ao criptografar o arquivo e salve para usar posteriormente quando quiser descriptografar o arquivo.

# Descriptografar um arquivo

```
guardian.descriptografar_arquivo()
```

Copie o caminho para o arquivo criptografado e cole no terminal. **C:\Users\Melissa\Desktop\ufpi/logo.png.encrypted**

**Ao selecionar o arquivo criptogrado é importante colocar .encrypted após o nome do arquivo pois é o tipo do arquivo.**

Cole a senha que você salvou quando for pedida a senha de descriptografia.

Para a abrir o arquivo descriptografado selecione um programa para o tipo específico de arquivo que foi criptografado. **Ex.: Windows Media Player para vídeos ou músicas.**

### Licença

O CryptoGuardian é distribuído sob a [Licença MIT](https://opensource.org/licenses/MIT). Você é livre para usar, modificar e distribuir este pacote de acordo com os termos da licença.
