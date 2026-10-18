from kbitfont import KbitGlyph, KbitProps
from pixel_font_builder import Glyph


def create_glyph_from_kbit(name: str, kbit_glyph: KbitGlyph, kbit_props: KbitProps) -> Glyph:
    return Glyph(
        name=name,
        horizontal_offset=(kbit_glyph.x, kbit_glyph.y - kbit_glyph.height),
        advance_width=kbit_glyph.advance,
        vertical_offset=(kbit_glyph.width // 2, kbit_props.em_ascent - kbit_glyph.y),
        advance_height=kbit_props.em_height,
        bitmap=[[0 if color <= 127 else 1 for color in bitmap_row] for bitmap_row in kbit_glyph.bitmap],
    )
