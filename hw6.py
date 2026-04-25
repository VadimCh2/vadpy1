from pywebio.input import input, select, slider
from pywebio.output import put_text, put_markdown

from hw6_logic import calculate_trip

def app():
    put_markdown("## 🏫 Організація поїздки")

    students = int(input("Кількість учнів:", type="number"))
    teachers = int(input("Кількість вчителів:", type="number"))

    transport = select("Оберіть транспорт:", ["Автобус 🚌", "Поїзд 🚆"])

    days = slider("Кількість днів:", min_value=0, max_value=14)

    result = calculate_trip(students, teachers, transport, days)

    if "error" in result:
        put_text("❌ " + result["error"])
        return

    put_markdown("## 📊 Результати")

    put_text(f"👥 Людей: {result['total_people']}")

    if result["transport"] == "Автобус 🚌":
        put_text(f"🚌 Автобусів: {result['buses']}")

    put_text(f"💸 Транспорт: {result['transport_cost']} грн")
    put_text(f"🏨 Проживання: {result['living_cost']} грн")

    if result["discount"] > 0:
        put_text(f"🎉 Знижка: {result['discount']} грн")

    put_markdown(f"## 💰 Всього: {result['total_cost']} грн")

app()