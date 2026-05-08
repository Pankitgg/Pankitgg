import random
import datetime

def generate_snake_svg(username):
    today = datetime.date.today()
    
    contributions = []
    for week_idx in range(52):
        week_data = []
        for day_idx in range(7):
            days_ago = (51 - week_idx) * 7 + (6 - day_idx)
            date = today - datetime.timedelta(days=days_ago)
            
            base_count = 0
            if date.weekday() < 5:
                base_count = random.randint(0, 8)
            else:
                base_count = random.randint(0, 3)
            
            if date.year == 2024 and date.month >= 10:
                base_count = random.randint(2, 15)
            elif date.year == 2025 and date.month <= 5:
                base_count = random.randint(3, 12)
            
            week_data.append(base_count)
        contributions.append(week_data)
    
    svg_parts = []
    svg_parts.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 120" fill="none">')
    svg_parts.append('  <rect width="820" height="120" fill="#0d1117"/>')
    
    for week_idx, week in enumerate(contributions[:52]):
        for day_idx, count in enumerate(week[:7]):
            x = week_idx * 16 + 5
            y = day_idx * 14 + 5
            
            if count == 0:
                fill_color = "#161b22"
            elif count < 5:
                fill_color = "#0e4429"
            elif count < 10:
                fill_color = "#006d32"
            elif count < 20:
                fill_color = "#26a641"
            else:
                fill_color = "#39d353"
            
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="{fill_color}"/>')
    
    snake_head_week = 51
    
    snake_positions = []
    for i in range(5):
        pos_week = max(0, snake_head_week - i)
        snake_positions.append((pos_week, 3))
    
    for i, (wx, wy) in enumerate(snake_positions):
        x = wx * 16 + 5
        y = wy * 14 + 5
        opacity = 1 - (i * 0.15)
        svg_parts.append(f'  <rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="#f0883e" opacity="{opacity}"/>')
    
    svg_parts.append('</svg>')
    
    return '\n'.join(svg_parts)

if __name__ == "__main__":
    username = "Pankitgg"
    svg_content = generate_snake_svg(username)
    with open("github-contribution-grid-snake.svg", "w") as f:
        f.write(svg_content)
    print("SVG generated successfully")