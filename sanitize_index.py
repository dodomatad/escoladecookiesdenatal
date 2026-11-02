import re

with open('pagina_vsl.html', 'r', encoding='utf-8', errors='ignore') as fp:
    html = fp.read()

# 1. Replace Donuts references
html = html.replace('Escola de Donuts', 'Escola de Cookies')
html = html.replace('Donuts caseiros', 'Cookies caseiros')
html = html.replace('em cada Donut', 'em cada Cookie')
html = html.replace('cada Donut', 'cada Cookie')

# 2. Unify checkout links
html = html.replace('https://pay.lowify.com.br/checkout?product_id=8iIi5R', 'https://app.cakto.com.br/checkout-builder/1248031')

# 3. Fix legal links in footer
pattern = r'<span class="hover:opacity-100 cursor-pointer transition-opacity">Pol[^<]+tica de Privacidade</span><span class="hidden sm:inline">\|</span><span class="hover:opacity-100 cursor-pointer transition-opacity">Termos de Uso</span>'
replacement = '<a href="politica-de-privacidade.html" target="_blank" class="hover:opacity-100 text-white underline transition-opacity">Política de Privacidade</a><span class="hidden sm:inline">|</span><a href="termos-de-uso.html" target="_blank" class="hover:opacity-100 text-white underline transition-opacity">Termos de Uso</a>'

html = re.sub(pattern, replacement, html)

# 4. Insert Meta Pixel base code in head
pixel_code = """
<!-- Meta Pixel Code Base (Insira seu ID real gerado no Gerenciador) -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
// Substitua SEU_PIXEL_ID pelo número do seu Pixel
var PIXEL_ID = 'SEU_PIXEL_ID';
if (PIXEL_ID && PIXEL_ID !== 'SEU_PIXEL_ID') {
    fbq('init', PIXEL_ID);
    fbq('track', 'PageView');
}
</script>
<!-- End Meta Pixel Code -->
"""

if '</head>' in html:
    html = html.replace('</head>', pixel_code + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as fp:
    fp.write(html)

print("index.html created successfully! Size:", len(html))

# Verify Donuts removal
print("Donuts count in index.html:", len(re.findall(r'donut', html, re.I)))
