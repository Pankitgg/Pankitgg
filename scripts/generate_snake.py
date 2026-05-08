import requests
import datetime
import calendar

def generate_snake_svg(username):
    today = datetime.date.today()
    year_ago = today - datetime.timedelta(days=364)
    
    url = f"https://api.github.com/users/{username}/contributions"
    headers = {"Accept": "application/vnd.github+json"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        contributions = response.json()
    except:
        contributions = []
    
    grid = []
    for week in contributions:
        week_data = []
        for day in week.get('contributionDays', []):
            week_data.append(day.get('contributionCount', 0))
        grid.append(week_data)
    
    if not grid:
        grid = [[0]*7 for _ in range(52)]
    
    svg_parts = []
    svg_parts.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 120" fill="none">')
    svg_parts.append('  <rect width="820" height="120" fill="#0d1117"/>')
    
    snake_color = "#3fb950"
    bg_color = "#161b22"
    empty_color = "#0d1117"
    
    for week_idx, week in enumerate(grid):
        for day_idx, count in enumerate(week):
            x = week_idx * 16 + 5
            y = day_idx * 14 + 5
            
            if count == 0:
                fill_color = empty_color
            elif count < 5:
                fill_color = "#238636"
            elif count < 10:
                fill_color = "#2ea043"
            elif count < 20:
                fill_color = "#3fb950"
            else:
                fill_color = "#56d364"
            
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="{fill_color}"/>')
    
    snake_positions = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]
    
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