// JavaScript interativo e acessibilidade para o Portal Ricardo Leon
document.addEventListener("DOMContentLoaded", () => {
  // 1. Menu Mobile Toggle
  const menuToggle = document.getElementById("menuToggle");
  const navLinks = document.getElementById("navLinks");

  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
    });
  }

  // 2. Alto Contraste (Acessibilidade WCAG)
  const contrastBtn = document.getElementById("toggleContrast");
  if (contrastBtn) {
    contrastBtn.addEventListener("click", () => {
      document.body.classList.toggle("high-contrast");
      const isContrast = document.body.classList.contains("high-contrast");
      localStorage.setItem("highContrast", isContrast ? "true" : "false");
    });

    if (localStorage.getItem("highContrast") === "true") {
      document.body.classList.add("high-contrast");
    }
  }

  // 3. Ajuste de Tamanho de Fonte (Acessibilidade)
  const fontIncreaseBtn = document.getElementById("increaseFont");
  const fontDecreaseBtn = document.getElementById("decreaseFont");
  const fontResetBtn = document.getElementById("resetFont");
  let currentZoom = 100;

  if (fontIncreaseBtn && fontDecreaseBtn) {
    fontIncreaseBtn.addEventListener("click", () => {
      if (currentZoom < 140) {
        currentZoom += 10;
        document.documentElement.style.fontSize = `${currentZoom}%`;
      }
    });

    fontDecreaseBtn.addEventListener("click", () => {
      if (currentZoom > 90) {
        currentZoom -= 10;
        document.documentElement.style.fontSize = `${currentZoom}%`;
      }
    });

    if (fontResetBtn) {
      fontResetBtn.addEventListener("click", () => {
        currentZoom = 100;
        document.documentElement.style.fontSize = "100%";
      });
    }
  }

  // 4. Copiar Chave PIX com Feedback
  const copyPixBtn = document.getElementById("copyPixBtn");
  const pixKeyText = document.getElementById("pixKeyText");

  if (copyPixBtn && pixKeyText) {
    copyPixBtn.addEventListener("click", () => {
      const key = pixKeyText.innerText.trim();
      navigator.clipboard.writeText(key).then(() => {
        const originalText = copyPixBtn.innerText;
        copyPixBtn.innerText = "Copiado com Sucesso! ✓";
        copyPixBtn.style.backgroundColor = "#15803d";
        setTimeout(() => {
          copyPixBtn.innerText = originalText;
          copyPixBtn.style.backgroundColor = "";
        }, 3000);
      });
    });
  }
});
