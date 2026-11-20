# Habotrappan: original image audit

Source pages inspected on20November2026: `/`, `/bildgalleri/`, `/om_oss/`, `/kontakt/`. Elementor homepage stylesheet `post-5.css` identifies the actual current hero `trappsteg.jpg`. Public WordPress media metadata was read at `/wp-json/wp/v2/media?per_page=100` and individual attachment URLs; unrelated imported agency/demo assets were excluded.

## Current gallery and higher-resolution originals

The current gallery has9photos, with empty alt/caption fields and neutral attachment names. There are no named models, customers, locations, budgets, dates, project outcomes or descriptions to preserve. The delivered9 gallery items keep that exact source set and order, with newly written visible-feature descriptions. Categories are editorial, not a manufacturer product classification.

The first3 photos are delivered from their exact current gallery originals (IDs542,537,536). Six gallery images have higher-resolution photographs in the same site's public media library. The photographs, objects, angle and crop were visually compared at large scale; only the same source photograph was substituted for its smaller crop:

| Current gallery attachment | Delivered source attachment | Description |
|---|---|---|
|562|550|white staircase, wallpaper|
|560|543|dark treads and white balustrade, foreground post|
|557|551|outdoor wooden stair and deck|
|561|549|dark-post staircase with glass panels|
|559|555|stair viewed from above with painting/lamp|
|558|553|close detail of wood-and-glass railing|

An initial candidate548 was rejected as an alternate angle of the same-looking interior, and the correct exact-photo543 was selected instead. No alternate angles were silently grouped as a project. Each gallery photo remains one independent inspiration item. Current cropped-source dimensions and delivered-source IDs are retained in assets.json.

## Hero options and other material

`hero.avif` is source attachment556 (also duplicated as38 in the public WordPress library), an original stair photograph1536×2048 proportionally compressed to1425×1900. It is suitable for a clean architectural crop through the middle of the staircase. Its source is the public library, not the current9-photo gallery, and it is not assigned a new customer case or project name.

`trappsteg.avif` is the actual homepage background photograph1306×701. `racke-landskap.avif` is a2000×1200 original library crop of the same wooden balustrade photograph also stored in the site's home-media variants. `hantverk.avif` is the original tools still life; it is an illustration of craft and is not claimed to depict current workshop operations. `trappa-hem.avif` is the current homepage's square stair photo.

`verkstad.avif` is the actual contact-page building photograph. No new date, new-expansion claim or opening-hours information is attached. `jan-englof.avif` is the larger source-library portrait explicitly titled Jan Englöf (attachment119), visually the same owner portrait used in the current `/om_oss/` page. No new identity or date is inferred.

## Original logo

The current source logo is `logga-original.jpg`,585×60, a green Habo Trappindustri wordmark on an opaque white JPEG canvas. Its exact bytes are preserved as `assets/logo.jpg`; source and delivered hashes are identical. No actual transparent PNG/SVG version of this wordmark was found in the site's public attachment metadata. The older `HT-logo.jpg` has a different layout and was deliberately not substituted for the current mark.

The delivered JPEG is **not** transparent. Root may use CSS blend/filter treatment to show the original faithfully on a selected canvas; no pixels were edited, no lettering was reconstructed, and no new logo was generated. At small native size, respect its limited585px width and preserve its aspect ratio.

## Processing and verification

Only EXIF orientation, proportional downscaling when larger than1900px, and AVIF encoding were applied to photo files. There is no AI generation, element insertion/removal, retouching or manufactured before/after. Original downloads remain temporary; finalfiles and their original-source/delivered SHA256, dimensions, bytecounts and provenance are in assets.json. The17deliveredassets total about2MB. The final contact sheet was inspected for correct objects, portraits and crop pairings. Unknown wood species, structural engineering, finish systems, measurements and safety-compliance claims are not invented.
