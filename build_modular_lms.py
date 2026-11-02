import os
import re

print("Iniciando construcao da Area de Membros Modular...")

# Caminhos dos arquivos
BASE_DIR = r"C:\Users\dedeu\Desktop\ofertacookienovo"

# HTML COMPLETO VIP (Acesso a todos os 4 modulos)
def generate_completo_html():
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow, noarchive">
  <title>Área de Membros VIP | Escola de Cookies & Confeitaria</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Montserrat', 'sans-serif'],
          },
          colors: {
            brand: {
              cream: '#FAF7F2',
              card: '#191211',
              cardHover: '#231816',
              border: '#2A1F1D',
              primary: '#E15A4F',
              primaryHover: '#C9473C',
              pink: '#DB2777',
              pinkHover: '#BE185D',
              amber: '#D97706',
              green: '#16A34A',
              dark: '#0F0A0A',
            }
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Montserrat', sans-serif; background-color: #0F0A0A; color: #F5EFEB; scroll-behavior: smooth; }
    .card-hover { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    .card-hover:hover { transform: translateY(-4px); border-color: rgba(225, 90, 79, 0.5); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.7), 0 0 25px rgba(225, 90, 79, 0.2); }
    .module-card { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; }
    .module-card:hover { transform: translateY(-5px); }
    .module-card.active-module { border-color: #E15A4F; box-shadow: 0 0 25px rgba(225, 90, 79, 0.4); background: linear-gradient(180deg, #261614 0%, #191211 100%); }
    .fade-in-content { animation: fadeIn 0.35s ease-out forwards; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .custom-scrollbar::-webkit-scrollbar { height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: #191211; border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #E15A4F; border-radius: 9999px; }
  </style>
</head>
<body class="min-h-screen flex flex-col bg-[#0F0A0A] text-stone-100">

  <!-- TOP BAR NOTIFICAÇÃO -->
  <div class="bg-gradient-to-r from-red-950/80 via-[#E15A4F]/20 to-amber-950/80 border-b border-[#E15A4F]/30 py-2 px-4 text-center text-xs font-semibold text-stone-200">
    ✨ Bem-vinda à sua Formação Profissional! Todos os módulos estão 100% liberados para download e estudo.
  </div>

  <!-- HEADER -->
  <header class="bg-[#1A1110]/95 backdrop-blur border-b border-stone-800 sticky top-0 z-50 shadow-xl">
    <div class="max-w-6xl mx-auto px-4 py-3 sm:py-4 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-gradient-to-br from-[#E15A4F] to-amber-700 flex items-center justify-center text-2xl shadow-md shadow-[#E15A4F]/20">
          🍪
        </div>
        <div>
          <h1 class="text-base sm:text-xl font-black text-[#E15A4F] tracking-tight leading-none">ESCOLA DE COOKIES & CONFEITARIA</h1>
          <p class="text-[10px] sm:text-xs font-bold text-[#D4A373] uppercase tracking-wider mt-1">Área de Membros • Pacote Completo VIP (Acesso Total)</p>
        </div>
      </div>
      <div class="flex items-center gap-2 sm:gap-3">
        <span class="inline-flex items-center gap-1.5 bg-emerald-950/90 text-emerald-400 border border-emerald-500/30 text-[11px] sm:text-xs font-bold px-3 py-1.5 rounded-full shadow-sm">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Acesso VIP Vitalício
        </span>
      </div>
    </div>
  </header>

  <!-- BANNER DE BOAS-VINDAS -->
  <section class="max-w-6xl mx-auto px-4 pt-6 pb-2">
    <div class="w-full rounded-2xl sm:rounded-3xl overflow-hidden shadow-2xl border border-amber-500/20 bg-[#1A0505]">
      <img src="banner_confeitaria.jpg" alt="Curso de Confeitaria - Do Básico ao Profissional" class="w-full h-auto object-cover block" loading="eager" fetchpriority="high">
    </div>
  </section>

  <!-- MAIN CONTAINER -->
  <main class="max-w-6xl mx-auto px-4 py-8 flex-1 w-full space-y-10">

    <!-- SELETOR DE MÓDULOS (LMS HUB) -->
    <section id="modulos-hub" class="scroll-mt-24">
      <div class="text-center sm:text-left mb-6 pb-3 border-b border-stone-800 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
        <div>
          <span class="inline-flex items-center gap-1.5 bg-[#E15A4F]/10 text-[#E15A4F] border border-[#E15A4F]/20 font-bold text-xs uppercase px-3 py-1 rounded-full mb-2">
            🎓 Plataforma de Aulas & Apostilas
          </span>
          <h2 class="text-2xl sm:text-3xl font-black text-white">Escolha o Módulo para Estudar</h2>
          <p class="text-sm text-stone-400 mt-1">Clique em um dos módulos abaixo para abrir instantaneamente os materiais e ferramentas:</p>
        </div>
        <div class="text-xs text-stone-400 font-semibold bg-stone-900/80 px-3 py-2 rounded-lg border border-stone-800">
          📚 <strong class="text-white">18 Materiais</strong> Disponíveis
        </div>
      </div>

      <!-- GRID DOS 4 MÓDULOS -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

        <!-- CARD MÓDULO 1 -->
        <div onclick="selectModule(1)" id="btn-card-mod-1" class="module-card active-module bg-[#191211] rounded-2xl p-4 border border-stone-800 flex flex-col justify-between group">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80">
              <img src="carrossel_cookies_recheados.jpg" alt="Cookies & Delivery iFood" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-[#E15A4F] text-white text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-md shadow-md">
                Módulo 1
              </span>
              <span class="absolute bottom-2 right-2 bg-black/80 backdrop-blur-sm text-stone-200 text-[10px] font-bold px-2 py-0.5 rounded border border-white/10">
                8 Materiais
              </span>
            </div>
            <h3 class="text-base font-bold text-white group-hover:text-[#E15A4F] transition-colors leading-snug">
              Cookies Lucrativos & Delivery iFood
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              Receitas campeãs americanas, validade, fotografia e delivery passo a passo no iFood.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-[#E15A4F] flex items-center gap-1">
              <span class="status-indicator">● Ativo agora</span>
            </span>
            <span class="text-xs font-extrabold text-white bg-[#E15A4F] px-3 py-1.5 rounded-lg shadow-sm group-hover:bg-[#C9473C] transition-colors">
              Ver Aulas →
            </span>
          </div>
        </div>

        <!-- CARD MÓDULO 2 -->
        <div onclick="selectModule(2)" id="btn-card-mod-2" class="module-card bg-[#191211] rounded-2xl p-4 border border-stone-800 flex flex-col justify-between group">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80">
              <img src="carrossel_brownies_gourmet.jpg" alt="Sobremesas & Brownies" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-[#DB2777] text-white text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-md shadow-md">
                Módulo 2
              </span>
              <span class="absolute bottom-2 right-2 bg-black/80 backdrop-blur-sm text-stone-200 text-[10px] font-bold px-2 py-0.5 rounded border border-white/10">
                3 Materiais
              </span>
            </div>
            <h3 class="text-base font-bold text-white group-hover:text-[#DB2777] transition-colors leading-snug">
              Sobremesas Gourmet & Brownies
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              Brownies com casquinha crocante, Copos da Felicidade e Tortas Mousse aeradas.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-[#DB2777] flex items-center gap-1">
              <span>● Liberado VIP</span>
            </span>
            <span class="text-xs font-extrabold text-white bg-stone-800 px-3 py-1.5 rounded-lg group-hover:bg-[#DB2777] transition-colors">
              Ver Aulas →
            </span>
          </div>
        </div>

        <!-- CARD MÓDULO 3 -->
        <div onclick="selectModule(3)" id="btn-card-mod-3" class="module-card bg-[#191211] rounded-2xl p-4 border border-stone-800 flex flex-col justify-between group">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80">
              <img src="carrossel_brigadeiros_gourmet.jpg" alt="Doces Finos" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-amber-600 text-white text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-md shadow-md">
                Módulo 3
              </span>
              <span class="absolute bottom-2 right-2 bg-black/80 backdrop-blur-sm text-stone-200 text-[10px] font-bold px-2 py-0.5 rounded border border-white/10">
                3 Materiais
              </span>
            </div>
            <h3 class="text-base font-bold text-white group-hover:text-amber-500 transition-colors leading-snug">
              Brigadeiros, Cupcakes & Macarons
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              60 receitas nobres de brigadeiros de vitrine, cupcakes fofos e macarons franceses.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-amber-500 flex items-center gap-1">
              <span>● Liberado VIP</span>
            </span>
            <span class="text-xs font-extrabold text-white bg-stone-800 px-3 py-1.5 rounded-lg group-hover:bg-amber-600 transition-colors">
              Ver Aulas →
            </span>
          </div>
        </div>

        <!-- CARD MÓDULO 4 (BÔNUS SALGADOS) -->
        <div onclick="selectModule(4)" id="btn-card-mod-4" class="module-card bg-[#191211] rounded-2xl p-4 border border-stone-800 flex flex-col justify-between group">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80 bg-gradient-to-br from-amber-950 via-stone-900 to-amber-900 flex items-center justify-center">
              <div class="text-center p-2">
                <span class="text-4xl">🥐</span>
                <p class="text-[11px] font-black text-amber-400 mt-1 uppercase">Panificação Nobre</p>
              </div>
              <span class="absolute top-2 left-2 bg-emerald-600 text-white text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-md shadow-md">
                Bônus VIP
              </span>
              <span class="absolute bottom-2 right-2 bg-black/80 backdrop-blur-sm text-stone-200 text-[10px] font-bold px-2 py-0.5 rounded border border-white/10">
                4 Materiais
              </span>
            </div>
            <h3 class="text-base font-bold text-white group-hover:text-emerald-400 transition-colors leading-snug">
              Salgados Comerciais & Panificação
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              Top 10 Salgados assados, empadão de confeitaria e o Livro de Ouro da Panificação.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-emerald-400 flex items-center gap-1">
              <span>● Liberado VIP</span>
            </span>
            <span class="text-xs font-extrabold text-white bg-stone-800 px-3 py-1.5 rounded-lg group-hover:bg-emerald-600 transition-colors">
              Ver Aulas →
            </span>
          </div>
        </div>

      </div>
    </section>

    <!-- NAVEGAÇÃO RÁPIDA POR ABAS (STICKY TABS) -->
    <div id="module-tabs-nav" class="sticky top-[69px] z-40 bg-[#160E0D]/95 backdrop-blur-md py-3 border-y border-stone-800 -mx-4 px-4 shadow-md">
      <div class="max-w-6xl mx-auto flex items-center justify-start sm:justify-center gap-2 overflow-x-auto custom-scrollbar pb-1">
        <button onclick="selectModule(1)" id="tab-nav-1" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#E15A4F] text-white shadow-md shrink-0 transition-all">
          <span>🍪</span> Módulo 1: Cookies (8)
        </button>
        <button onclick="selectModule(2)" id="tab-nav-2" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-300 hover:text-white border border-stone-800 shrink-0 transition-all">
          <span>🍫</span> Módulo 2: Sobremesas (3)
        </button>
        <button onclick="selectModule(3)" id="tab-nav-3" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-300 hover:text-white border border-stone-800 shrink-0 transition-all">
          <span>🧁</span> Módulo 3: Doces Finos (3)
        </button>
        <button onclick="selectModule(4)" id="tab-nav-4" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-300 hover:text-white border border-stone-800 shrink-0 transition-all">
          <span>🥐</span> Módulo 4: Salgados (4)
        </button>
      </div>
    </div>

    <!-- ÁREA DE EXIBIÇÃO DE CONTEÚDO DOS MÓDULOS -->
    <div id="module-display-area" class="scroll-mt-36">

      <!-- ============================================== -->
      <!-- CONTEÚDO MÓDULO 1: COOKIES & DELIVERY (8 ITENS) -->
      <!-- ============================================== -->
      <section id="content-mod-1" class="module-content-pane fade-in-content">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 pb-4 border-b border-stone-800 gap-3">
          <div>
            <div class="inline-flex items-center gap-2 bg-[#E15A4F]/10 text-[#E15A4F] font-bold text-xs uppercase px-3 py-1 rounded-full mb-2 border border-[#E15A4F]/20">
              <span>🍪</span> Formação Principal
            </div>
            <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Módulo 1: Escola de Cookies & Delivery iFood</h3>
            <p class="text-sm text-stone-400 mt-1">Apostilas de receitas, manuais de venda no delivery e planilha de precificação automatizada</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="bg-emerald-950/80 text-emerald-400 border border-emerald-500/30 font-extrabold text-xs sm:text-sm px-3.5 py-1.5 rounded-full">
              ✓ 8 Materiais Liberados
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

          <!-- Item 1: Especialista em Cookies -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 via-amber-600/10 to-amber-950/40 border border-amber-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(245,158,11,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍪</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-[#E15A4F]">Curso Principal</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Especialista em Cookies</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Domine as massas perfeitas, técnicas de ponto, recheios irresistíveis e o padrão profissional que vende todo dia.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila Oficial (1,2 MB)</span>
              <a href="materiais/especialista-em-cookies.pdf" download="especialista-em-cookies.pdf" class="inline-flex items-center gap-1.5 bg-[#E15A4F] hover:bg-[#C9473C] text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 2: Manual do iFood Lucrativo -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-red-500/20 via-red-600/10 to-red-950/40 border border-red-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(239,68,68,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🛵</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-[#EA1D2C]">Guia Oficial iFood</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Manual do iFood Lucrativo</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Como cadastrar seu cardápio, criar combos magnéticos e posicionar sua loja no topo do aplicativo na sua região.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Manual Digital (3,4 MB)</span>
              <a href="materiais/manual-ifood-lucrativo.pdf" download="manual-ifood-lucrativo.pdf" class="inline-flex items-center gap-1.5 bg-[#EA1D2C] hover:bg-[#c41521] text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 3: Cookies para Delivery -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500/20 via-emerald-600/10 to-emerald-950/40 border border-emerald-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(16,185,129,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">📦</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Operação & Embalagem</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Cookies para Delivery</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Técnicas de conservação, transporte seguro sem quebrar o cookie e embalagens térmicas que encantam o cliente.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila Técnica (1,4 MB)</span>
              <a href="materiais/cookies-para-delivery.pdf" download="cookies-para-delivery.pdf" class="inline-flex items-center gap-1.5 bg-[#16A34A] hover:bg-[#15803D] text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 4: Masterclass Cookies -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-rose-500/20 via-rose-600/10 to-rose-950/40 border border-rose-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(244,63,94,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">⭐</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Conteúdo Avançado</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Apostila Masterclass Cookies</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Segredos de textura, crocância por fora e maciez por dentro que diferenciam seu produto da concorrência comum.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Masterclass (2,5 MB)</span>
              <a href="materiais/apostila-masterclass-cookies.pdf" download="apostila-masterclass-cookies.pdf" class="inline-flex items-center gap-1.5 bg-rose-600 hover:bg-rose-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 5: Cookies Tradicionais -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-600/20 via-orange-600/10 to-amber-950/40 border border-amber-600/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(245,158,11,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🧁</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-orange-400">Receitas Clássicas</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Cookies Tradicionais & Clássicos</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">As fórmulas consagradas que não saem de moda: gotas de chocolate meio amargo, baunilha clássica e red velvet.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Livro de Receitas (6,2 MB)</span>
              <a href="materiais/cookies-tradicionais-receitas-classicas.pdf" download="cookies-tradicionais-receitas-classicas.pdf" class="inline-flex items-center gap-1.5 bg-orange-600 hover:bg-orange-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 6: Guia de Precificação Profissional -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500/20 via-blue-600/10 to-blue-950/40 border border-blue-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(59,130,246,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">💰</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-blue-400">Gestão & Finanças</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Guia de Precificação Profissional</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Aprenda a calcular custos fixos, variáveis, taxas de entrega e sua margem de lucro real para nunca ter prejuízo.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Guia Financeiro (1,1 MB)</span>
              <a href="materiais/guia-de-precificacao-profissional.pdf" download="guia-de-precificacao-profissional.pdf" class="inline-flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 7: Planilha de Precificação -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-teal-500/20 via-teal-600/10 to-teal-950/40 border border-teal-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(20,184,166,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">📊</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Ferramenta Automática</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Planilha de Precificação</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Ferramenta prática e automatizada para calcular o preço exato de cada receita e garantir seu lucro com 1 clique.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📊 Planilha & Material (27 KB)</span>
              <a href="materiais/planilha-de-precificacao.pdf" download="planilha-de-precificacao.pdf" class="inline-flex items-center gap-1.5 bg-teal-700 hover:bg-teal-800 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 8: Estratégias Avançadas iFood -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500/20 via-purple-600/10 to-purple-950/40 border border-purple-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(168,85,247,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🚀</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Apostila Completa Delivery</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Estratégias Avançadas iFood</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Guia completo e aprofundado para alavancar pedidos diários e transformar sua loja em referência na cidade.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Livro Digital (94,8 MB)</span>
              <a href="materiais/estrategias-avancadas-ifood.pdf" download="estrategias-avancadas-ifood.pdf" class="inline-flex items-center gap-1.5 bg-purple-700 hover:bg-purple-800 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

        </div>

        <!-- BARRA INFERIOR DE NAVEGAÇÃO -->
        <div class="mt-8 p-4 rounded-xl bg-stone-900/60 border border-stone-800 flex items-center justify-between">
          <span class="text-xs text-stone-400 font-semibold">Concluiu os Cookies? Vá para o próximo:</span>
          <button onclick="selectModule(2)" class="inline-flex items-center gap-1.5 bg-[#DB2777] hover:bg-[#BE185D] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            Ir para Módulo 2: Sobremesas →
          </button>
        </div>
      </section>

      <!-- ============================================== -->
      <!-- CONTEÚDO MÓDULO 2: SOBREMESAS & BROWNIES (3 ITENS) -->
      <!-- ============================================== -->
      <section id="content-mod-2" class="module-content-pane hidden fade-in-content">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 pb-4 border-b border-stone-800 gap-3">
          <div>
            <div class="inline-flex items-center gap-2 bg-[#DB2777]/10 text-[#DB2777] font-bold text-xs uppercase px-3 py-1 rounded-full mb-2 border border-[#DB2777]/20">
              <span>🍫</span> Especial Confeitaria Fina
            </div>
            <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Módulo 2: Sobremesas Lucrativas & Brownies</h3>
            <p class="text-sm text-stone-400 mt-1">Apostilas de brownies gourmet, copos da felicidade e tortas mousse aeradas</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="bg-pink-950/80 text-pink-400 border border-pink-500/30 font-extrabold text-xs sm:text-sm px-3.5 py-1.5 rounded-full">
              ✓ 3 Materiais Liberados
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

          <!-- Item 9: Ana Brownie - Brownies Gourmet -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-600/30 via-amber-800/20 to-stone-950/50 border border-amber-600/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(217,119,6,0.3)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍫</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Curso Ana Brownie</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Brownies Gourmet Perfeitos</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
                  Casquinha brilhante, centro molhadinho, técnicas de corte, recheios em camadas e precificação comercial.
                </p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (1,1 MB)</span>
              <a href="materiais_sobremesas/ana-brownie-brownies-gourmet.pdf" download="ana-brownie-brownies-gourmet.pdf" class="inline-flex items-center gap-1.5 bg-[#DB2777] hover:bg-[#BE185D] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 10: Apostila Copos da Felicidade -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-pink-500/25 via-pink-600/15 to-pink-950/40 border border-pink-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(219,39,119,0.3)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍧</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-[#DB2777]">Campeão de Vendas Delivery</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Copos da Felicidade</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
                  Montagens irresistíveis em camadas, cremes aveludados, caldas especiais e decoração que atrai pedidos.
                </p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (10,8 MB)</span>
              <a href="materiais_sobremesas/apostila-copos-da-felicidade.pdf" download="apostila-copos-da-felicidade.pdf" class="inline-flex items-center gap-1.5 bg-[#DB2777] hover:bg-[#BE185D] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 11: Tortas Mousse Lucrativas -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500/25 via-pink-600/15 to-stone-950/40 border border-purple-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(168,85,247,0.3)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍰</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Cardápio de Alto Padrão</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Tortas Mousse Lucrativas</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
                  Bases crocantes, mousses aeradas que derretem na boca, espelhamento vitrine e alta margem de lucro.
                </p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (11,4 MB)</span>
              <a href="materiais_sobremesas/tortas-mousse-lucrativas.pdf" download="tortas-mousse-lucrativas.pdf" class="inline-flex items-center gap-1.5 bg-[#DB2777] hover:bg-[#BE185D] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

        </div>

        <!-- BARRA INFERIOR DE NAVEGAÇÃO -->
        <div class="mt-8 p-4 rounded-xl bg-stone-900/60 border border-stone-800 flex items-center justify-between">
          <button onclick="selectModule(1)" class="inline-flex items-center gap-1.5 bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            ← Voltar ao Módulo 1
          </button>
          <button onclick="selectModule(3)" class="inline-flex items-center gap-1.5 bg-amber-600 hover:bg-amber-500 text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            Ir para Módulo 3: Doces Finos →
          </button>
        </div>
      </section>

      <!-- ============================================== -->
      <!-- CONTEÚDO MÓDULO 3: BRIGADEIROS & MACARONS (3 ITENS) -->
      <!-- ============================================== -->
      <section id="content-mod-3" class="module-content-pane hidden fade-in-content">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 pb-4 border-b border-stone-800 gap-3">
          <div>
            <div class="inline-flex items-center gap-2 bg-amber-500/10 text-amber-400 font-bold text-xs uppercase px-3 py-1 rounded-full mb-2 border border-amber-500/20">
              <span>✨</span> Alta Confeitaria & Doces Finos
            </div>
            <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Módulo 3: Brigadeiros Gourmet, Cupcakes & Macarons</h3>
            <p class="text-sm text-stone-400 mt-1">Apostilas completas com 60 receitas de brigadeiros, cupcakes artesanais e macarons franceses</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="bg-amber-950/80 text-amber-400 border border-amber-500/30 font-extrabold text-xs sm:text-sm px-3.5 py-1.5 rounded-full">
              ✓ 3 Materiais Liberados
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

          <!-- Item 12: 60 Receitas de Brigadeiros -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/25 via-amber-700/15 to-stone-950/40 border border-amber-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(245,158,11,0.3)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍫</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Doces Tradicionais & Finos</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">60 Receitas de Brigadeiros</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
                  Ponto de enrolar perfeito, ponto de bico, sabores gourmet luxuosos, decorações nobres e validade prolongada.
                </p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (10,5 MB)</span>
              <a href="materiais_doces/brigadeiros-60-receitas.pdf" download="brigadeiros-60-receitas.pdf" class="inline-flex items-center gap-1.5 bg-[#E15A4F] hover:bg-[#C9473C] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 13: Cupcakes Gourmet -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-pink-500/25 via-pink-600/15 to-pink-950/40 border border-pink-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(219,39,119,0.3)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🧁</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-pink-400">Massas Fofas & Recheios</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Cupcakes Gourmet</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
                  Massas ultra macias, técnicas de recheio no centro, coberturas aveludadas que não derretem e apresentação vitrine.
                </p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (9,8 MB)</span>
              <a href="materiais_doces/cupcakes-gourmet.pdf" download="cupcakes-gourmet.pdf" class="inline-flex items-center gap-1.5 bg-[#DB2777] hover:bg-[#BE185D] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 14: Macarons Franceses -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/25 via-purple-600/15 to-stone-950/40 border border-indigo-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(99,102,241,0.3)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🥮</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Patisserie Francesa</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Macarons Franceses</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
                  Técnica do merengue italiano e francês, macaronagem precisa, saia perfeita, secagem e recheios estáveis.
                </p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (130 MB)</span>
              <a href="materiais_doces/macarons-franceses.pdf" download="macarons-franceses.pdf" class="inline-flex items-center gap-1.5 bg-[#6366F1] hover:bg-[#4F46E5] text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-xl transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

        </div>

        <!-- BARRA INFERIOR DE NAVEGAÇÃO -->
        <div class="mt-8 p-4 rounded-xl bg-stone-900/60 border border-stone-800 flex items-center justify-between">
          <button onclick="selectModule(2)" class="inline-flex items-center gap-1.5 bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            ← Voltar ao Módulo 2
          </button>
          <button onclick="selectModule(4)" class="inline-flex items-center gap-1.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            Ir para Módulo 4: Bônus Salgados →
          </button>
        </div>
      </section>

      <!-- ============================================== -->
      <!-- CONTEÚDO MÓDULO 4: BÔNUS SALGADOS & PANIFICAÇÃO (4 ITENS) -->
      <!-- ============================================== -->
      <section id="content-mod-4" class="module-content-pane hidden fade-in-content">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 pb-4 border-b border-stone-800 gap-3">
          <div>
            <div class="inline-flex items-center gap-2 bg-emerald-500/10 text-emerald-400 font-bold text-xs uppercase px-3 py-1 rounded-full mb-2 border border-emerald-500/20">
              <span>🥐</span> Bônus Exclusivo VIP
            </div>
            <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Módulo 4: Salgados Comerciais & Panificação</h3>
            <p class="text-sm text-stone-400 mt-1">Apostilas completas de salgados assados de vitrine, massa de empadão e segredos da panificação clássica</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="bg-emerald-950/80 text-emerald-400 border border-emerald-500/30 font-extrabold text-xs sm:text-sm px-3.5 py-1.5 rounded-full">
              ✓ 4 Materiais Liberados
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

          <!-- Item 15: Curso de Salgados Top 10 -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 via-amber-600/10 to-amber-950/40 border border-amber-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(245,158,11,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🥐</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Salgados Campeões</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Curso de Salgados Top 10</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">As 10 receitas mais pedidas de lanchonetes e encomendas: coxinhas, quibes, risoles e técnicas de congelamento.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (1,2 MB)</span>
              <a href="materiais_salgados/curso-de-salgados-top-10.pdf" download="curso-de-salgados-top-10.pdf" class="inline-flex items-center gap-1.5 bg-amber-600 hover:bg-amber-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 16: Empadão Gourmet -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-yellow-500/20 via-amber-600/10 to-yellow-950/40 border border-yellow-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(234,179,8,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🥧</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-yellow-400">Massa Podre que Derrete</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Empadão Tradicional & Lucrativo</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Massa nobre que desmancha na boca, recheios cremosos de frango com catupiry, palmito e montagem em fôrmas comerciais.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (6,9 MB)</span>
              <a href="materiais_salgados/empadao.pdf" download="empadao.pdf" class="inline-flex items-center gap-1.5 bg-yellow-600 hover:bg-yellow-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 17: Livro de Ouro da Panificação -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-orange-500/20 via-amber-600/10 to-orange-950/40 border border-orange-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(249,115,22,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍞</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-orange-400">Enciclopédia Completa</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">O Livro de Ouro da Panificação</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Fermentação, pães artesanais, modelagens profissionais e controle de temperatura da massa.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Livro Completo (29,4 MB)</span>
              <a href="materiais_salgados/o-livro-de-ouro-da-panificacao.pdf" download="o-livro-de-ouro-da-panificacao.pdf" class="inline-flex items-center gap-1.5 bg-orange-600 hover:bg-orange-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 18: Salgados Assados -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500/20 via-emerald-600/10 to-emerald-950/40 border border-emerald-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(16,185,129,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🥪</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Assados de Sucesso</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Salgados Assados Práticos</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Esfihas abertas, enroladinhos e empadas com excelente durabilidade e menor custo operacional.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila (1,1 MB)</span>
              <a href="materiais_salgados/salgados-assados.pdf" download="salgados-assados.pdf" class="inline-flex items-center gap-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

        </div>

        <!-- BARRA INFERIOR DE NAVEGAÇÃO -->
        <div class="mt-8 p-4 rounded-xl bg-stone-900/60 border border-stone-800 flex items-center justify-between">
          <button onclick="selectModule(3)" class="inline-flex items-center gap-1.5 bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            ← Voltar ao Módulo 3
          </button>
          <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="inline-flex items-center gap-1.5 bg-stone-800 hover:bg-stone-700 text-stone-300 hover:text-white text-xs sm:text-sm font-bold px-4 py-2 rounded-lg transition-all">
            ↑ Voltar ao Topo
          </button>
        </div>
      </section>

    </div>

  </main>

  <!-- FOOTER -->
  <footer class="bg-[#120B0B] border-t border-stone-800 py-8 text-center text-stone-400 text-sm mt-12">
    <div class="max-w-4xl mx-auto px-4">
      <p class="font-bold text-[#E15A4F] mb-1">Escola de Cookies & Confeitaria © Todos os direitos reservados</p>
      <p class="text-xs text-stone-500">Em caso de dúvidas sobre o acesso aos materiais, entre em contato com nosso suporte.</p>
    </div>
  </footer>

  <!-- SCRIPT DE NAVEGAÇÃO DOS MÓDULOS -->
  <script>
    function selectModule(modNum) {
      // 1. Esconder todas as seções de conteúdo
      for (let i = 1; i <= 4; i++) {
        const pane = document.getElementById('content-mod-' + i);
        if (pane) {
          pane.classList.add('hidden');
        }
        
        // Resetar estilos das abas sticky
        const tabNav = document.getElementById('tab-nav-' + i);
        if (tabNav) {
          tabNav.className = 'tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-300 hover:text-white border border-stone-800 shrink-0 transition-all';
        }

        // Resetar cards do Hub
        const cardBtn = document.getElementById('btn-card-mod-' + i);
        if (cardBtn) {
          cardBtn.classList.remove('active-module');
        }
      }

      // 2. Ativar a seção clicada
      const activePane = document.getElementById('content-mod-' + modNum);
      if (activePane) {
        activePane.classList.remove('hidden');
      }

      // 3. Destacar a aba ativa
      const activeTabNav = document.getElementById('tab-nav-' + modNum);
      if (activeTabNav) {
        if (modNum === 1) activeTabNav.className = 'tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#E15A4F] text-white shadow-lg shrink-0 transition-all border border-[#E15A4F]';
        else if (modNum === 2) activeTabNav.className = 'tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#DB2777] text-white shadow-lg shrink-0 transition-all border border-[#DB2777]';
        else if (modNum === 3) activeTabNav.className = 'tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-amber-600 text-white shadow-lg shrink-0 transition-all border border-amber-500';
        else if (modNum === 4) activeTabNav.className = 'tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-emerald-600 text-white shadow-lg shrink-0 transition-all border border-emerald-500';
      }

      // 4. Destacar o card no Hub
      const activeCardBtn = document.getElementById('btn-card-mod-' + modNum);
      if (activeCardBtn) {
        activeCardBtn.classList.add('active-module');
      }

      // 5. Rolagem suave até a área de conteúdo
      const displayArea = document.getElementById('module-display-area');
      if (displayArea) {
        const yOffset = -90;
        const y = displayArea.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  </script>

</body>
</html>'''

# Escreve completo/index.html e completo.html e membros.html
completo_content = generate_completo_html()

with open(os.path.join(BASE_DIR, "completo", "index.html"), "w", encoding="utf-8") as f:
    f.write(completo_content)

with open(os.path.join(BASE_DIR, "completo.html"), "w", encoding="utf-8") as f:
    f.write(completo_content)

with open(os.path.join(BASE_DIR, "membros.html"), "w", encoding="utf-8") as f:
    f.write(completo_content)

print("OK: completo/index.html, completo.html e membros.html atualizados!")

# HTML PRINCIPAL (Plano Basico com Modulo 1 liberado e Modulos 2, 3 e 4 bloqueados com modal de Upgrade VIP)
def generate_principal_html():
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow, noarchive">
  <title>Área de Membros | Escola de Cookies & Confeitaria</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Montserrat', 'sans-serif'],
          },
          colors: {
            brand: {
              cream: '#FAF7F2',
              card: '#191211',
              cardHover: '#231816',
              border: '#2A1F1D',
              primary: '#E15A4F',
              primaryHover: '#C9473C',
              pink: '#DB2777',
              pinkHover: '#BE185D',
              amber: '#D97706',
              green: '#16A34A',
              dark: '#0F0A0A',
            }
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Montserrat', sans-serif; background-color: #0F0A0A; color: #F5EFEB; scroll-behavior: smooth; }
    .card-hover { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    .card-hover:hover { transform: translateY(-4px); border-color: rgba(225, 90, 79, 0.5); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.7), 0 0 25px rgba(225, 90, 79, 0.2); }
    .module-card { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; }
    .module-card:hover { transform: translateY(-5px); }
    .module-card.active-module { border-color: #E15A4F; box-shadow: 0 0 25px rgba(225, 90, 79, 0.4); background: linear-gradient(180deg, #261614 0%, #191211 100%); }
    .fade-in-content { animation: fadeIn 0.35s ease-out forwards; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .btn-pulse { animation: pulseBtn 2s infinite; }
    @keyframes pulseBtn {
      0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(22, 163, 74, 0.7); }
      50% { transform: scale(1.03); box-shadow: 0 0 0 10px rgba(22, 163, 74, 0); }
    }
    .custom-scrollbar::-webkit-scrollbar { height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: #191211; border-radius: 9999px; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #E15A4F; border-radius: 9999px; }
  </style>
</head>
<body class="min-h-screen flex flex-col bg-[#0F0A0A] text-stone-100">

  <!-- TOP BAR NOTIFICAÇÃO -->
  <div class="bg-gradient-to-r from-stone-900 via-stone-800 to-stone-900 border-b border-stone-800 py-2 px-4 text-center text-xs font-semibold text-stone-300">
    🍪 Bem-vinda! Seu Plano Básico de Cookies está liberado. <button onclick="openUpgradeModal()" class="text-[#E15A4F] hover:underline font-extrabold ml-1">Clique aqui para desbloquear os outros módulos VIP com desconto especial</button>
  </div>

  <!-- HEADER -->
  <header class="bg-[#1A1110]/95 backdrop-blur border-b border-stone-800 sticky top-0 z-50 shadow-xl">
    <div class="max-w-6xl mx-auto px-4 py-3 sm:py-4 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-gradient-to-br from-[#E15A4F] to-amber-700 flex items-center justify-center text-2xl shadow-md shadow-[#E15A4F]/20">
          🍪
        </div>
        <div>
          <h1 class="text-base sm:text-xl font-black text-[#E15A4F] tracking-tight leading-none">ESCOLA DE COOKIES & CONFEITARIA</h1>
          <p class="text-[10px] sm:text-xs font-bold text-stone-400 uppercase tracking-wider mt-1">Área de Membros • Plano Básico</p>
        </div>
      </div>
      <div class="flex items-center gap-2 sm:gap-3">
        <button onclick="openUpgradeModal()" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-amber-600 to-[#E15A4F] hover:opacity-90 text-white text-[11px] sm:text-xs font-extrabold px-3 py-1.5 rounded-full shadow-md transition-all">
          <span>👑</span> Desbloquear VIP
        </button>
      </div>
    </div>
  </header>

  <!-- BANNER DE BOAS-VINDAS -->
  <section class="max-w-6xl mx-auto px-4 pt-6 pb-2">
    <div class="w-full rounded-2xl sm:rounded-3xl overflow-hidden shadow-2xl border border-amber-500/20 bg-[#1A0505]">
      <img src="banner_confeitaria.jpg" alt="Curso de Confeitaria - Do Básico ao Profissional" class="w-full h-auto object-cover block" loading="eager" fetchpriority="high">
    </div>
  </section>

  <!-- MAIN CONTAINER -->
  <main class="max-w-6xl mx-auto px-4 py-8 flex-1 w-full space-y-10">

    <!-- SELETOR DE MÓDULOS (LMS HUB) -->
    <section id="modulos-hub" class="scroll-mt-24">
      <div class="text-center sm:text-left mb-6 pb-3 border-b border-stone-800 flex flex-col sm:flex-row sm:items-end justify-between gap-2">
        <div>
          <span class="inline-flex items-center gap-1.5 bg-[#E15A4F]/10 text-[#E15A4F] border border-[#E15A4F]/20 font-bold text-xs uppercase px-3 py-1 rounded-full mb-2">
            🎓 Plataforma de Aulas & Apostilas
          </span>
          <h2 class="text-2xl sm:text-3xl font-black text-white">Escolha o Módulo para Estudar</h2>
          <p class="text-sm text-stone-400 mt-1">Seu plano inclui o Módulo 1 completo. Os módulos VIP podem ser liberados a qualquer momento:</p>
        </div>
        <div class="text-xs text-stone-400 font-semibold bg-stone-900/80 px-3 py-2 rounded-lg border border-stone-800">
          🍪 <strong class="text-white">8 Materiais</strong> Liberados no seu Plano
        </div>
      </div>

      <!-- GRID DOS 4 MÓDULOS -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

        <!-- CARD MÓDULO 1 (LIBERADO) -->
        <div onclick="selectModule(1)" id="btn-card-mod-1" class="module-card active-module bg-[#191211] rounded-2xl p-4 border border-stone-800 flex flex-col justify-between group">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80">
              <img src="carrossel_cookies_recheados.jpg" alt="Cookies & Delivery iFood" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-[#E15A4F] text-white text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-md shadow-md">
                Módulo 1
              </span>
              <span class="absolute bottom-2 right-2 bg-black/80 backdrop-blur-sm text-stone-200 text-[10px] font-bold px-2 py-0.5 rounded border border-white/10">
                8 Materiais
              </span>
            </div>
            <h3 class="text-base font-bold text-white group-hover:text-[#E15A4F] transition-colors leading-snug">
              Cookies Lucrativos & Delivery iFood
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              Receitas campeãs americanas, validade, fotografia e delivery passo a passo no iFood.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-[#E15A4F] flex items-center gap-1">
              <span>● Liberado</span>
            </span>
            <span class="text-xs font-extrabold text-white bg-[#E15A4F] px-3 py-1.5 rounded-lg shadow-sm group-hover:bg-[#C9473C] transition-colors">
              Ver Aulas →
            </span>
          </div>
        </div>

        <!-- CARD MÓDULO 2 (BLOQUEADO) -->
        <div onclick="openUpgradeModal('Sobremesas Lucrativas & Brownies')" id="btn-card-mod-2" class="module-card bg-[#140E0E] rounded-2xl p-4 border border-stone-800/60 flex flex-col justify-between group opacity-85 hover:opacity-100">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80">
              <img src="carrossel_brownies_gourmet.jpg" alt="Sobremesas & Brownies" class="w-full h-full object-cover grayscale-[30%] group-hover:scale-105 transition-transform duration-300">
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <span class="bg-black/80 backdrop-blur text-amber-400 border border-amber-500/40 text-xs font-black px-3 py-1.5 rounded-full shadow-lg">
                  🔒 VIP Exclusivo
                </span>
              </div>
            </div>
            <h3 class="text-base font-bold text-stone-300 group-hover:text-[#DB2777] transition-colors leading-snug">
              Sobremesas Gourmet & Brownies
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              Brownies com casquinha crocante, Copos da Felicidade e Tortas Mousse aeradas.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-amber-400 flex items-center gap-1">
              <span>🔒 Bloqueado</span>
            </span>
            <span class="text-xs font-extrabold text-amber-400 bg-amber-950/60 border border-amber-500/30 px-3 py-1.5 rounded-lg group-hover:bg-amber-600 group-hover:text-white transition-colors">
              Desbloquear →
            </span>
          </div>
        </div>

        <!-- CARD MÓDULO 3 (BLOQUEADO) -->
        <div onclick="openUpgradeModal('Brigadeiros Gourmet, Cupcakes & Macarons')" id="btn-card-mod-3" class="module-card bg-[#140E0E] rounded-2xl p-4 border border-stone-800/60 flex flex-col justify-between group opacity-85 hover:opacity-100">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80">
              <img src="carrossel_brigadeiros_gourmet.jpg" alt="Doces Finos" class="w-full h-full object-cover grayscale-[30%] group-hover:scale-105 transition-transform duration-300">
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <span class="bg-black/80 backdrop-blur text-amber-400 border border-amber-500/40 text-xs font-black px-3 py-1.5 rounded-full shadow-lg">
                  🔒 VIP Exclusivo
                </span>
              </div>
            </div>
            <h3 class="text-base font-bold text-stone-300 group-hover:text-amber-500 transition-colors leading-snug">
              Brigadeiros, Cupcakes & Macarons
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              60 receitas nobres de brigadeiros de vitrine, cupcakes fofos e macarons franceses.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-amber-400 flex items-center gap-1">
              <span>🔒 Bloqueado</span>
            </span>
            <span class="text-xs font-extrabold text-amber-400 bg-amber-950/60 border border-amber-500/30 px-3 py-1.5 rounded-lg group-hover:bg-amber-600 group-hover:text-white transition-colors">
              Desbloquear →
            </span>
          </div>
        </div>

        <!-- CARD MÓDULO 4 (BLOQUEADO) -->
        <div onclick="openUpgradeModal('Salgados Comerciais & Panificação')" id="btn-card-mod-4" class="module-card bg-[#140E0E] rounded-2xl p-4 border border-stone-800/60 flex flex-col justify-between group opacity-85 hover:opacity-100">
          <div>
            <div class="relative w-full h-36 rounded-xl overflow-hidden mb-3 border border-stone-800/80 bg-stone-900 flex items-center justify-center">
              <div class="text-center p-2 opacity-50">
                <span class="text-4xl">🥐</span>
              </div>
              <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                <span class="bg-black/80 backdrop-blur text-amber-400 border border-amber-500/40 text-xs font-black px-3 py-1.5 rounded-full shadow-lg">
                  🔒 VIP Exclusivo
                </span>
              </div>
            </div>
            <h3 class="text-base font-bold text-stone-300 group-hover:text-emerald-400 transition-colors leading-snug">
              Salgados Comerciais & Panificação
            </h3>
            <p class="text-xs text-stone-400 mt-1.5 line-clamp-2 leading-relaxed">
              Top 10 Salgados assados, empadão de confeitaria e o Livro de Ouro da Panificação.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-stone-800/80 flex items-center justify-between">
            <span class="text-[11px] font-bold text-amber-400 flex items-center gap-1">
              <span>🔒 Bloqueado</span>
            </span>
            <span class="text-xs font-extrabold text-amber-400 bg-amber-950/60 border border-amber-500/30 px-3 py-1.5 rounded-lg group-hover:bg-amber-600 group-hover:text-white transition-colors">
              Desbloquear →
            </span>
          </div>
        </div>

      </div>
    </section>

    <!-- NAVEGAÇÃO RÁPIDA POR ABAS (STICKY TABS) -->
    <div id="module-tabs-nav" class="sticky top-[69px] z-40 bg-[#160E0D]/95 backdrop-blur-md py-3 border-y border-stone-800 -mx-4 px-4 shadow-md">
      <div class="max-w-6xl mx-auto flex items-center justify-start sm:justify-center gap-2 overflow-x-auto custom-scrollbar pb-1">
        <button onclick="selectModule(1)" id="tab-nav-1" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#E15A4F] text-white shadow-md shrink-0 transition-all">
          <span>🍪</span> Módulo 1: Cookies (8)
        </button>
        <button onclick="openUpgradeModal('Módulo 2: Sobremesas')" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-400 hover:text-amber-400 border border-stone-800 shrink-0 transition-all">
          <span>🔒</span> Módulo 2: Sobremesas
        </button>
        <button onclick="openUpgradeModal('Módulo 3: Doces Finos')" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-400 hover:text-amber-400 border border-stone-800 shrink-0 transition-all">
          <span>🔒</span> Módulo 3: Doces Finos
        </button>
        <button onclick="openUpgradeModal('Módulo 4: Salgados')" class="tab-button inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#1F1615] text-stone-400 hover:text-amber-400 border border-stone-800 shrink-0 transition-all">
          <span>🔒</span> Módulo 4: Salgados
        </button>
      </div>
    </div>

    <!-- ÁREA DE EXIBIÇÃO DE CONTEÚDO DO MÓDULO 1 -->
    <div id="module-display-area" class="scroll-mt-36">

      <!-- ============================================== -->
      <!-- CONTEÚDO MÓDULO 1: COOKIES & DELIVERY (8 ITENS) -->
      <!-- ============================================== -->
      <section id="content-mod-1" class="module-content-pane fade-in-content">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 pb-4 border-b border-stone-800 gap-3">
          <div>
            <div class="inline-flex items-center gap-2 bg-[#E15A4F]/10 text-[#E15A4F] font-bold text-xs uppercase px-3 py-1 rounded-full mb-2 border border-[#E15A4F]/20">
              <span>🍪</span> Formação Principal
            </div>
            <h3 class="text-2xl sm:text-3xl font-extrabold text-white">Módulo 1: Escola de Cookies & Delivery iFood</h3>
            <p class="text-sm text-stone-400 mt-1">Apostilas de receitas, manuais de venda no delivery e planilha de precificação automatizada</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="bg-emerald-950/80 text-emerald-400 border border-emerald-500/30 font-extrabold text-xs sm:text-sm px-3.5 py-1.5 rounded-full">
              ✓ 8 Materiais Liberados
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

          <!-- Item 1: Especialista em Cookies -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500/20 via-amber-600/10 to-amber-950/40 border border-amber-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(245,158,11,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🍪</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-[#E15A4F]">Curso Principal</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Especialista em Cookies</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Domine as massas perfeitas, técnicas de ponto, recheios irresistíveis e o padrão profissional que vende todo dia.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila Oficial (1,2 MB)</span>
              <a href="materiais/especialista-em-cookies.pdf" download="especialista-em-cookies.pdf" class="inline-flex items-center gap-1.5 bg-[#E15A4F] hover:bg-[#C9473C] text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 2: Manual do iFood Lucrativo -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-red-500/20 via-red-600/10 to-red-950/40 border border-red-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(239,68,68,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🛵</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-[#EA1D2C]">Guia Oficial iFood</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Manual do iFood Lucrativo</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Como cadastrar seu cardápio, criar combos magnéticos e posicionar sua loja no topo do aplicativo na sua região.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Manual Digital (3,4 MB)</span>
              <a href="materiais/manual-ifood-lucrativo.pdf" download="manual-ifood-lucrativo.pdf" class="inline-flex items-center gap-1.5 bg-[#EA1D2C] hover:bg-[#c41521] text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 3: Cookies para Delivery -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500/20 via-emerald-600/10 to-emerald-950/40 border border-emerald-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(16,185,129,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">📦</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Operação & Embalagem</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Cookies para Delivery</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Técnicas de conservação, transporte seguro sem quebrar o cookie e embalagens térmicas que encantam o cliente.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Apostila Técnica (1,4 MB)</span>
              <a href="materiais/cookies-para-delivery.pdf" download="cookies-para-delivery.pdf" class="inline-flex items-center gap-1.5 bg-[#16A34A] hover:bg-[#15803D] text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 4: Masterclass Cookies -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-rose-500/20 via-rose-600/10 to-rose-950/40 border border-rose-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(244,63,94,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">⭐</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Conteúdo Avançado</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Apostila Masterclass Cookies</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Segredos de textura, crocância por fora e maciez por dentro que diferenciam seu produto da concorrência comum.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Masterclass (2,5 MB)</span>
              <a href="materiais/apostila-masterclass-cookies.pdf" download="apostila-masterclass-cookies.pdf" class="inline-flex items-center gap-1.5 bg-rose-600 hover:bg-rose-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 5: Cookies Tradicionais -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-600/20 via-orange-600/10 to-amber-950/40 border border-amber-600/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(245,158,11,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🧁</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-orange-400">Receitas Clássicas</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Cookies Tradicionais & Clássicos</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">As fórmulas consagradas que não saem de moda: gotas de chocolate meio amargo, baunilha clássica e red velvet.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Livro de Receitas (6,2 MB)</span>
              <a href="materiais/cookies-tradicionais-receitas-classicas.pdf" download="cookies-tradicionais-receitas-classicas.pdf" class="inline-flex items-center gap-1.5 bg-orange-600 hover:bg-orange-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 6: Guia de Precificação Profissional -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500/20 via-blue-600/10 to-blue-950/40 border border-blue-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(59,130,246,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">💰</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-blue-400">Gestão & Finanças</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Guia de Precificação Profissional</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Aprenda a calcular custos fixos, variáveis, taxas de entrega e sua margem de lucro real para nunca ter prejuízo.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Guia Financeiro (1,1 MB)</span>
              <a href="materiais/guia-de-precificacao-profissional.pdf" download="guia-de-precificacao-profissional.pdf" class="inline-flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 7: Planilha de Precificação -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-teal-500/20 via-teal-600/10 to-teal-950/40 border border-teal-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(20,184,166,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">📊</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Ferramenta Automática</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Planilha de Precificação</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Ferramenta prática e automatizada para calcular o preço exato de cada receita e garantir seu lucro com 1 clique.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📊 Planilha & Material (27 KB)</span>
              <a href="materiais/planilha-de-precificacao.pdf" download="planilha-de-precificacao.pdf" class="inline-flex items-center gap-1.5 bg-teal-700 hover:bg-teal-800 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Item 8: Estratégias Avançadas iFood -->
          <div class="bg-[#191211] rounded-2xl p-5 sm:p-6 border border-stone-800/80 shadow-lg card-hover flex flex-col justify-between">
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500/20 via-purple-600/10 to-purple-950/40 border border-purple-500/40 flex items-center justify-center shrink-0 shadow-[0_0_20px_rgba(168,85,247,0.25)] relative group overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <span class="text-4xl filter drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)] transform group-hover:scale-110 transition-transform duration-300">🚀</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Apostila Completa Delivery</span>
                <h4 class="text-lg sm:text-xl font-bold text-white mt-1 leading-snug">Estratégias Avançadas iFood</h4>
                <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">Guia completo e aprofundado para alavancar pedidos diários e transformar sua loja em referência na cidade.</p>
              </div>
            </div>
            <div class="pt-4 border-t border-stone-800 flex items-center justify-between mt-auto">
              <span class="text-xs font-semibold text-stone-500">📄 Livro Digital (94,8 MB)</span>
              <a href="materiais/estrategias-avancadas-ifood.pdf" download="estrategias-avancadas-ifood.pdf" class="inline-flex items-center gap-1.5 bg-purple-700 hover:bg-purple-800 text-white text-sm font-bold px-4 py-2 rounded-lg transition-colors shadow-sm">
                Acessar a aula
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
              </a>
            </div>
          </div>

        </div>

        <!-- BOX UPSELL DE DESBLOQUEIO VIP NO RODAPÉ -->
        <div class="mt-12 p-6 sm:p-8 rounded-2xl bg-gradient-to-br from-[#1E1110] via-[#2D1614] to-[#170E0D] border-2 border-amber-500/40 shadow-2xl relative overflow-hidden text-center sm:text-left flex flex-col sm:flex-row items-center justify-between gap-6">
          <div class="max-w-xl">
            <span class="inline-flex items-center gap-1.5 bg-amber-500/20 text-amber-300 font-black text-xs uppercase px-3 py-1 rounded-full mb-3 border border-amber-500/30">
              👑 Upgrade Recomendado
            </span>
            <h4 class="text-xl sm:text-2xl font-black text-white">Desbloqueie os Outros 3 Módulos com 85% OFF</h4>
            <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
              Leve agora as apostilas completas de <strong>Brownies Gourmet, Copos da Felicidade, Tortas Mousse, 60 Receitas de Brigadeiros, Macarons Franceses e Salgados Nobres</strong>.
            </p>
          </div>
          <div class="shrink-0 text-center">
            <p class="text-xs text-stone-400 line-through">De R$ 97,00</p>
            <p class="text-2xl sm:text-3xl font-black text-emerald-400">Por R$ 14,90</p>
            <p class="text-[10px] text-stone-400 uppercase font-semibold mb-3">Pagamento Único • Acesso Imediato</p>
            <a href="https://app.mivvo.com.br/checkout/cf9bbf6c-9100-4fb3-9179-b2400e2a8c22" target="_blank" class="btn-pulse inline-flex items-center justify-center gap-2 bg-gradient-to-r from-emerald-600 to-green-600 hover:from-emerald-500 hover:to-green-500 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-lg shadow-emerald-900/40 transition-all">
              DESBLOQUEAR TUDO AGORA ➔
            </a>
          </div>
        </div>

      </section>

    </div>

  </main>

  <!-- MODAL DE UPGRADE VIP -->
  <div id="upgrade-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-[#1A1110] border-2 border-amber-500/50 rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative animate-in fade-in zoom-in-95 duration-200">
      <button onclick="closeUpgradeModal()" class="absolute top-4 right-4 text-stone-400 hover:text-white bg-stone-800/80 hover:bg-stone-700 w-8 h-8 rounded-full flex items-center justify-center transition-colors">
        ✕
      </button>

      <div class="text-center">
        <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-amber-500 to-red-600 mx-auto flex items-center justify-center text-3xl shadow-lg shadow-amber-500/20 mb-4">
          🔒
        </div>
        <span class="inline-block bg-amber-500/20 text-amber-400 text-xs font-black uppercase px-3 py-1 rounded-full border border-amber-500/30 mb-2">
          Conteúdo Exclusivo VIP
        </span>
        <h3 id="modal-module-title" class="text-xl sm:text-2xl font-black text-white">
          Módulo Bloqueado no seu Plano
        </h3>
        <p class="text-xs sm:text-sm text-stone-300 mt-2 leading-relaxed">
          Este conteúdo faz parte da nossa <strong>Formação Completa VIP</strong>. Desbloqueie agora com acesso vitalício imediato a:
        </p>

        <div class="my-5 p-4 rounded-xl bg-stone-900/90 border border-stone-800 text-left space-y-2 text-xs text-stone-200">
          <div class="flex items-center gap-2">
            <span class="text-emerald-400">✓</span> <span><strong>Módulo 2:</strong> Brownies Gourmet, Copos da Felicidade & Mousses</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-400">✓</span> <span><strong>Módulo 3:</strong> 60 Brigadeiros, Cupcakes & Macarons Franceses</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-400">✓</span> <span><strong>Módulo 4:</strong> Bônus Salgados Comerciais & Panificação Nobre</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-emerald-400">✓</span> <span>Planilhas de Precificação e Fichas Técnicas extras</span>
          </div>
        </div>

        <div class="mb-5">
          <p class="text-xs text-stone-400 line-through">Valor normal: R$ 97,00</p>
          <p class="text-3xl font-black text-emerald-400">R$ 14,90 <span class="text-xs font-medium text-stone-300">(taxa única)</span></p>
        </div>

        <a href="https://app.mivvo.com.br/checkout/cf9bbf6c-9100-4fb3-9179-b2400e2a8c22" target="_blank" class="btn-pulse block w-full py-4 px-6 rounded-xl bg-gradient-to-r from-emerald-600 to-green-600 hover:from-emerald-500 hover:to-green-500 text-white font-black text-sm uppercase tracking-wider shadow-lg shadow-emerald-950/60 transition-all">
          SIM! QUERO LIBERAR MEU ACESSO VIP ➔
        </a>

        <button onclick="closeUpgradeModal()" class="mt-3 text-xs text-stone-500 hover:text-stone-300 underline">
          Voltar e continuar estudando Cookies no Módulo 1
        </button>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="bg-[#120B0B] border-t border-stone-800 py-8 text-center text-stone-400 text-sm mt-12">
    <div class="max-w-4xl mx-auto px-4">
      <p class="font-bold text-[#E15A4F] mb-1">Escola de Cookies & Confeitaria © Todos os direitos reservados</p>
      <p class="text-xs text-stone-500">Em caso de dúvidas sobre o acesso aos materiais, entre em contato com nosso suporte.</p>
    </div>
  </footer>

  <!-- SCRIPT -->
  <script>
    function selectModule(modNum) {
      if (modNum === 1) {
        const displayArea = document.getElementById('module-display-area');
        if (displayArea) {
          const yOffset = -90;
          const y = displayArea.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      } else {
        openUpgradeModal();
      }
    }

    function openUpgradeModal(moduleName) {
      const modal = document.getElementById('upgrade-modal');
      const title = document.getElementById('modal-module-title');
      if (moduleName && title) {
        title.innerText = 'Desbloquear ' + moduleName;
      }
      if (modal) {
        modal.classList.remove('hidden');
      }
    }

    function closeUpgradeModal() {
      const modal = document.getElementById('upgrade-modal');
      if (modal) {
        modal.classList.add('hidden');
      }
    }

    // Fechar modal ao clicar fora
    window.onclick = function(event) {
      const modal = document.getElementById('upgrade-modal');
      if (event.target === modal) {
        closeUpgradeModal();
      }
    }
  </script>

</body>
</html>'''

# Escreve principal/index.html e principal.html
principal_content = generate_principal_html()

with open(os.path.join(BASE_DIR, "principal", "index.html"), "w", encoding="utf-8") as f:
    f.write(principal_content)

with open(os.path.join(BASE_DIR, "principal.html"), "w", encoding="utf-8") as f:
    f.write(principal_content)

print("OK: principal/index.html e principal.html atualizados!")
print("PROCESSO CONCLUIDO COM SUCESSO!")
