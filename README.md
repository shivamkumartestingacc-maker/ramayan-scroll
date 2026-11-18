# Ramayan Scroll

A scroll-driven, canvas-rendered visual narrative built from star particles. Reference images are sampled into weighted particle clouds; scroll progress (`uP`) moves each star from its starting position toward its final home. Seven animated chapters build from a dark sky through the ocean, Ananta, the canopy, Sudarshana, the lotus, and Narayana, followed by a held end frame.

> **Repository status:** This checkout currently contains only this README. The notes below are the project brief and implementation contract for the HTML/canvas experience.

## The experience

### The 7 chapters

1. **Before.** A black screen, then stars switch on one at a time: first a few, then many.
2. **The Ocean.** A sea of blue stars spreads out from the centre and rolls in slow waves.
3. **Ananta.** The serpent’s coils light up along their length as they wind through the ocean.
4. **The Canopy.** The hoods rise out of the ocean and settle into place.
5. **Sudarshana.** The chakra grows from a single point into gold rings, with the inner rings spinning faster.
6. **The Lotus.** It starts as a bud and opens outward from its heart.
7. **Narayana.** Every star in the sky flies into place: crown first, then the face, then the arms.

### End frame

The end frame is a held composition, not an eighth chapter. It uses the final frame from the supplied reference image: Vishnu on the right, the ocean of stars along the bottom, and “Om Namo Narayanaya” with a closing line in the empty left space.

## Making the text easy to read

- On desktop, all text sits in the left third over empty sky, with a soft dark gradient behind it.
- Headlines are large serif (Fraunces). Body text is 17.5px at high contrast.
- Each panel only appears while its chapter is fully on screen.
- On phone, text moves to the bottom with a darker gradient behind it.

### Editing content

All display copy lives in one clearly marked block of panels near the top of the HTML, one panel per chapter. Change the wording inside that block; the animation, layout, and chapter timing should not need to change.

## How particles are made

1. Each reference image is drawn to a canvas and read as pixels.
2. A density map (CLAHE-style brightness plus edge boost) sets where stars go: brighter areas get more stars.
3. Each star samples the source colour at its pixel, normalised, then brightness-scaled.
4. Position = pixel → world coordinates (`wx`, `wy`), plus a depth term from brightness and a gaussian jitter.
5. Each star gets `from` (start point), `to` (target), `delay`, `kind`, and `size`. Sizes are mostly 0.8–1.25, ~12% are 1.4–2, and ~1% are 2.6–3.6.
6. The shader interpolates `from → home` by scroll progress `uP`, with per-kind rules: the ocean rises, coils reveal, the lotus opens from its centre, and the chakra spins.
7. Empty space is skipped by repeated weighted sampling (`while (m > 0)`), so the figure is denser than the background.

## Known rough spots

- At the end of the Lotus chapter, the lotus glows quite brightly and loses its petal shape.
- The chakra looks like a bright disc during its chapter. Its rings only read clearly in the final frame.
- On phone, the end frame crops in on his face and the chakra is cut off.
- On narrow screens, Indra and the chakra are too close. Mobile is still cramped and this remains unresolved.

## Fonts and screenshots

Existing screenshots used fallback fonts because the test browser had no internet; they do not show the intended typography. New font files are pending and should be swapped in when they arrive. The real fonts will appear once they are loaded.

## Problems hit

- Blurry particles → switched to crisp points with a tight halo.
- Devotee and hood looked cut out → rendered the full serpent as its own star cloud.
- Serpent came only from below → it now gathers from random sky positions.
- Clutter between Indra and Vishnu → moved DPOS and the ocean camera shot, and pulled back the final camera.
- Final chapter too slow → shortened the hold to 2.5s and matched the scroll speed.
- Local test server returned 404 → restarted from the correct folder.
- Narrow screens: Indra and the chakra too close. Mobile is still cramped; unresolved.

## Local testing

Serve from the directory containing the HTML and its reference images. Starting the test server from the wrong folder caused the local 404s noted above.
