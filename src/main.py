import asyncio
import random
import time

import flet as ft


def main(page: ft.Page):
    page.title = "Reflex Arcade"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 12

    mode = "idle"
    round_id = 0
    started_at = 0.0
    best_ms = None

    prompt = ft.Text("TAP TO START", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900)
    tap_zone = ft.Container(
        height=68,
        bgcolor=ft.Colors.CYAN_200,
        border_radius=14,
        alignment=ft.Alignment.CENTER,
        content=prompt,
    )
    best_value = ft.Text("—", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200)
    last_value = ft.Text("—", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    def set_zone(label: str, color: str):
        prompt.value = label
        tap_zone.bgcolor = color

    async def reveal_signal(token: int):
        nonlocal mode, started_at
        await asyncio.sleep(random.uniform(1.4, 3.2))
        if mode == "waiting" and token == round_id:
            mode = "go"
            started_at = time.perf_counter()
            set_zone("TAP NOW!", ft.Colors.GREEN_400)
            page.update()

    async def tap():
        nonlocal mode, round_id, started_at, best_ms
        if mode == "waiting":
            round_id += 1
            mode = "idle"
            set_zone("TOO SOON!", ft.Colors.AMBER_400)
        elif mode == "go":
            elapsed = round((time.perf_counter() - started_at) * 1000)
            mode = "done"
            last_value.value = f"{elapsed} ms"
            if best_ms is None or elapsed < best_ms:
                best_ms = elapsed
                best_value.value = f"{best_ms} ms"
            set_zone(f"{elapsed} ms", ft.Colors.CYAN_200)
        else:
            round_id += 1
            mode = "waiting"
            set_zone("WAIT FOR GREEN", ft.Colors.AMBER_400)
            asyncio.create_task(reveal_signal(round_id))
        page.update()

    tap_zone.on_click = tap

    brand_name = ft.Text("REFLEX ARCADE", size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    quick_test = ft.Text("QUICK TEST", size=10, color=ft.Colors.CYAN_200)
    heading = ft.Text("Beat the signal.", size=23, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    subtitle = ft.Text("Wait for green, then tap as fast as you can.", size=13, color=ft.Colors.BLUE_GREY_100)
    best_label = ft.Text("PERSONAL BEST", size=9, color=ft.Colors.BLUE_GREY_100)
    last_label = ft.Text("LAST ROUND", size=9, color=ft.Colors.BLUE_GREY_100)

    width = min(520, max(240, (page.width or 520) - 32))
    panel = ft.Container(
        width=width,
        padding=16,
        bgcolor=ft.Colors.BLUE_GREY_800,
        border=ft.Border.all(1, ft.Colors.BLUE_GREY_700),
        border_radius=22,
        content=ft.Column(
            tight=True,
            spacing=9,
            controls=[
                ft.Row(
                    spacing=8,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(tight=True, spacing=8, controls=[
                            ft.Icon(ft.Icons.BOLT, size=18, color=ft.Colors.CYAN_200),
                            brand_name,
                        ]),
                        quick_test,
                    ],
                ),
                heading,
                subtitle,
                tap_zone,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(tight=True, spacing=2, controls=[best_label, best_value]),
                        ft.Column(
                            tight=True,
                            spacing=2,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            controls=[last_label, last_value],
                        ),
                    ],
                ),
            ],
        ),
    )

    theme_label = ft.Text("DARK", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200)
    theme_switch = ft.Switch(
        value=True,
        active_color=ft.Colors.CYAN_200,
        active_track_color=ft.Colors.BLUE_GREY_700,
    )

    def change_theme(e):
        dark = e.control.value
        page.theme_mode = ft.ThemeMode.DARK if dark else ft.ThemeMode.LIGHT
        page.bgcolor = ft.Colors.BLUE_GREY_900 if dark else ft.Colors.BLUE_GREY_50
        panel.bgcolor = ft.Colors.BLUE_GREY_800 if dark else ft.Colors.WHITE
        panel.border = ft.Border.all(1, ft.Colors.BLUE_GREY_700 if dark else ft.Colors.BLUE_GREY_200)
        text_color = ft.Colors.WHITE if dark else ft.Colors.BLUE_GREY_900
        secondary_color = ft.Colors.BLUE_GREY_100 if dark else ft.Colors.BLUE_GREY_700
        accent_color = ft.Colors.CYAN_200 if dark else ft.Colors.CYAN_700
        heading.color = text_color
        brand_name.color = text_color
        last_value.color = text_color
        quick_test.color = accent_color
        best_value.color = accent_color
        subtitle.color = secondary_color
        best_label.color = secondary_color
        last_label.color = secondary_color
        theme_label.value = "DARK" if dark else "LIGHT"
        theme_label.color = accent_color
        page.update()

    theme_switch.on_change = change_theme
    toolbar = ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[ft.Row(tight=True, spacing=4, controls=[theme_label, theme_switch])],
    )
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                toolbar,
                ft.Container(expand=True, alignment=ft.Alignment.CENTER, content=panel),
            ],
        )
    )


ft.run(main)
