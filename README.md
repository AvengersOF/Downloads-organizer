# DownloadOrganizer

Automatiza a organização da pasta **Downloads**, movendo arquivos para subpastas de acordo com o tipo.

---

## Estrutura do Projeto

```
DownloadOrganizer
organizer.py       
README.md          
dist/
     organizer.exe  
```

---

## Como funciona

O script detecta automaticamente a pasta `Downloads` do usuário e organiza os arquivos na seguinte forma:
Cria uma pasta documentos para pdfs e docxs;
Cria uma pasta so para arquivos de imagens;
Cria uma pasta para arquivos de audio;


---

## Como usar

### Executável (sem Python)
Baixe o `organizer.exe` na pasta `dist/` e execute diretamente. Não requer instalação.

## Gerar o executável (opcional)

## Observações

- Arquivos sem extensão reconhecida são movidos para a pasta **Outros**.
- As subpastas são criadas automaticamente caso não existam.
- O script não afeta pastas, apenas arquivos.

---

**Autor:** Kennedy Claudio Alves Barbosa 
**Linguagem:** Python 3  
**Licença:** MIT
