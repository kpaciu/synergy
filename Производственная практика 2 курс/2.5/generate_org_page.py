# -*- coding: utf-8 -*-
import json, sys, html, pathlib

def make_font_links(primary, fallbacks):
    names = [primary] + list(fallbacks or [])
    links = []
    for name in names:
        # Простая эвристика: подключаем ссылку Google Fonts,
        # если имя похоже на шрифт без специальных символов.
        q = name.strip().replace(" ", "+")
        if q:
            links.append(f'<link href="https://fonts.googleapis.com/css2?family={q}:wght@300;400;600&display=swap" rel="stylesheet">')
    return "\n    ".join(links)

def css_font_family(primary, fallbacks):
    def qt(s): 
        s = s.strip()
        return f"'{s}'" if " " in s else s
    fam = [qt(primary)] + [qt(f) for f in (fallbacks or [])] + ["sans-serif"]
    return ", ".join(fam)

def render(data: dict) -> str:
    name = html.escape(data.get("name","[Название организации]"))
    short_name = html.escape(data.get("short_name",""))
    legal_form = html.escape(data.get("legal_form",""))
    address = html.escape(data.get("address",""))
    website = html.escape(data.get("website",""))
    about = html.escape(data.get("about",""))
    services = data.get("services", [])
    contacts = data.get("contacts", {})
    primary_font = data.get("primary_font", "Inter")
    fallback_fonts = data.get("fallback_fonts", ["Roboto","Open Sans","Montserrat","PT Sans","Source Sans Pro"])

    font_links = make_font_links(primary_font, fallback_fonts)
    font_family = css_font_family(primary_font, fallback_fonts)

    services_html = "".join(f"<li>{html.escape(s)}</li>" for s in services)
    contacts_html = "".join(f"<li><strong>{html.escape(k)}:</strong> {html.escape(str(v))}</li>" for k,v in contacts.items())
    fallback_preview = "".join(
        f"<div style='font-family:{css_font_family(f,[*fallback_fonts])}; margin:8px 0;'><em>Предпросмотр {html.escape(f)}</em>: Быстрая коричневая лисица прыгает через ленивую собаку 0123456789</div>"
        for f in fallback_fonts
    )

    return f"""<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{name}</title>
    {font_links}
    <style>
      :root {{
        --text-color: #222;
        --muted: #666;
        --accent: #0b69ff;
        --bg: #fafafa;
      }}
      html, body {{
        margin: 0; padding: 0;
        background: var(--bg);
        color: var(--text-color);
        font-family: {font_family};
        line-height: 1.55;
      }}
      .container {{ max-width: 960px; margin: 0 auto; padding: 24px; }}
      header h1 {{ margin: 0 0 4px 0; font-size: 28px; }}
      header .sub {{ color: var(--muted); margin-bottom: 16px; }}
      section {{ background: white; border-radius: 12px; padding: 20px; margin: 16px 0; box-shadow: 0 1px 3px rgba(0,0,0,.05); }}
      h2 {{ margin-top: 0; font-size: 20px; }}
      a {{ color: var(--accent); text-decoration: none; }}
      a:hover {{ text-decoration: underline; }}
      ul {{ margin: 8px 0 0 18px; }}
      footer {{ font-size: 13px; color: var(--muted); margin: 24px 0; }}
      .grid {{ display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }}
      .chip {{ display:inline-block; padding:4px 10px; border-radius:999px; background:#eef4ff; margin:4px 8px 0 0; font-size:13px; }}
    </style>
  </head>
  <body>
    <div class="container">
      <header>
        <h1>{name}</h1>
        <div class="sub">{short_name} • {legal_form}</div>
        <div class="sub">Адрес: {address} · Сайт: <a href="{website}" target="_blank" rel="noopener">{website}</a></div>
      </header>

      <section>
        <h2>О компании</h2>
        <p>{about}</p>
      </section>

      <section>
        <h2>Основные услуги</h2>
        <ul>{services_html}</ul>
      </section>

      <section>
        <h2>Контакты</h2>
        <ul>{contacts_html}</ul>
      </section>

      <section>
        <h2>Шрифты</h2>
        <p>Основной шрифт: <strong>{html.escape(primary_font)}</strong>. Альтернативы:</p>
        <div>{fallback_preview}</div>
      </section>

      <footer>
        Сгенерировано автоматически · Редактируйте файл <code>org.json</code> и перегенерируйте страницу.
      </footer>
    </div>
  </body>
</html>"""

def main():
    if len(sys.argv) < 2:
        print("Использование: python generate_org_page.py org.json")
        sys.exit(2)
    input_path = pathlib.Path(sys.argv[1])
    out_dir = input_path.parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    html_text = render(data)
    (out_dir / "index.html").write_text(html_text, encoding="utf-8")
    print(f"Готово: {out_dir / 'index.html'}")

if __name__ == "__main__":
    main()
