# Wallpapers

A desktop wallpaper collection, organised by theme. Every image is committed here, so the repo works as a Git/Nix input without fetching anything.

## Layout

| Folder | Files | Contents |
| --- | --- | --- |
| `sci-fi/` | 21 | Atmospheric, cosmic and industrial-noir artwork, including the originally curated set |
| `illustration/` | 19 | Painted and cartoon scenes, anime frames, character art |
| `photography/` | 14 | Unsplash photography, landscapes, city and nature shots |
| `minimal/` | 16 | Flat vector and single-subject pieces |
| `retro/` | 8 | Game, terminal and FOSS theme art, gruvbox variants |
| `collections/doctor-who/` | 11 | Doctor Who set |
| `collections/stalenhag/` | 59 | Simon Stålenhag set, all 3440 × 1440 |

Resolutions are whatever the source provided, so they range from 1600 px wide up to 7680 px. Files are unmodified originals; no crops or re-encodes.

## Use as a Nix flake input

In `repparw/nix/modules/aspects/style.nix`, add:

```nix
flake-file.inputs.wallpapers = {
  url = "github:repparw/wallpapers";
  flake = false;
};
```

The repo itself does **not** need a `flake.nix`. In the existing `stylix` `let` block, replace the current external `pkgs.fetchurl` image expression with:

```nix
inputImage = "${inputs.wallpapers}/wallpapers/sci-fi/violet-monolith.png";
```

Any file works the same way. Keep the existing `pkgs.runCommand` dimming pipeline and `stylix.image = wallpaper` configuration unchanged. Since the Nix repo uses `flake-file`, regenerate its `flake.nix` using the existing `write-flake` workflow, then update the lock file.

## Rights and provenance

Two images were generated for this collection and carry no license yet: `sci-fi/violet-monolith.png` and `sci-fi/rainy-megacity.png`.

Eleven files in `sci-fi/` were downloaded from wallpaper sites and are third-party artwork redistributed here without permission. Wallpaper Abyss labels several "Free For Private, Personal Use," which is not a grant to republish; Bethesda's Starfield art is publisher copyright; two more are unverified. Their sources:

| File | Creator | Source |
| --- | --- | --- |
| `sci-fi/dystopian-dreams.png` | robokoboto | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1384548) |
| `sci-fi/shattered-space.jpg` | Bethesda Game Studios | [Official wallpaper](https://bethesda.net/en/game/starfield/media/wallpaper/starfield-shattered-space-wallpaper) |
| `sci-fi/derelict-orbital-citadel.jpg` | Paul Chadeisson | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1269192) |
| `sci-fi/celestial-megaship.jpg` | AI-generated / publisher Fred | [backiee](https://backiee.com/wallpaper/celestial-megaship-amidst-galactic-fog/302530) |
| `sci-fi/sci-fi-city.jpg` | Annibale Siconolfi | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1108470) |
| `sci-fi/futuristic-sci-fi-cityscape.jpg` | Annibale Siconolfi | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=1223603) |
| `sci-fi/futuristic-space-colony.jpg` | Paul Chadeisson | [Wallpaper Abyss](https://wall.alphacoders.com/big.php?i=928392) |
| `sci-fi/planet-among-stars.jpg` | Unverified | [HDQ Walls](https://hdqwalls.com/planet-science-fiction-among-stars-4k-wallpaper) |
| `sci-fi/cosmic-pyramids.jpg` | Unverified | [HDQ Walls](https://images.hdqwalls.com/download/cosmic-pyramids-ancient-future-yf-3840x2160.jpg) |
| `sci-fi/remember-me-slum-neoparis.jpg` | Paul Chadeisson | [ArtStation](https://www.artstation.com/artwork/zmx6) |
| `sci-fi/museum-alien-life.jpg` | Creator unverified | [Behance](https://www.behance.net/gallery/106183577/The-Museum-of-Alien-Life) |

The rest were collected locally with no recorded source. Where a filename carries a photographer name and number, the work came from Unsplash and falls under the Unsplash license. Everything else — including the Doctor Who and Simon Stålenhag sets, and the anime, game and cartoon pieces — is copyrighted work with no license granted.

Treat this repository as private until the rights are cleared or the files are replaced with original art. There is no blanket license for the collection.

<details>
<summary><b>sci-fi/</b> — 21 files</summary>

- `902435.jpg`
- `alien.png`
- `celestial-megaship.jpg`
- `cosmic-pyramids.jpg`
- `cosmos.png`
- `derelict-orbital-citadel.jpg`
- `dystopian-dreams.png`
- `escape-velocity.jpg`
- `fsociety.jpg`
- `futuristic-sci-fi-cityscape.jpg`
- `futuristic-space-colony.jpg`
- `mountains-on-mars.png`
- `museum-alien-life.jpg`
- `noir.png`
- `planet-among-stars.jpg`
- `rainy-megacity.png`
- `remember-me-slum-neoparis.jpg`
- `sci-fi-city.jpg`
- `shattered-space.jpg`
- `valley.png`
- `violet-monolith.png`

</details>

<details>
<summary><b>illustration/</b> — 19 files</summary>

- `calvin.png`
- `car.png`
- `cat.png`
- `cloud-storage.png`
- `coffee-pixels.png`
- `coffee.png`
- `dragon-ball-simple.png`
- `ghost.png`
- `heart-points.png`
- `maru-pink.png`
- `nordish.png`
- `pixar-lamp.png`
- `polaroids.jpg`
- `samurai.png`
- `shack.png`
- `street.png`
- `studio.png`
- `totoro.png`
- `war.png`

</details>

<details>
<summary><b>photography/</b> — 14 files</summary>

- `alistair-mackenzie-779903-unsplash.jpg`
- `aperture-vintage-318404-unsplash.jpg`
- `autumn.png`
- `evening-sky.png`
- `forest.png`
- `highway.jpg`
- `jakob-dalbjorn-249730-unsplash.jpg`
- `john-fowler-1072143-unsplash.jpg`
- `jr-korpa-529187-unsplash.jpg`
- `lucas-davies-507237-unsplash.jpg`
- `mountain.png`
- `nature.png`
- `pink-flower.jpg`
- `record.png`

</details>

<details>
<summary><b>minimal/</b> — 16 files</summary>

- `abduction.png`
- `autumn-is-near.png`
- `dots.png`
- `lighty.png`
- `modern-labyrinth.png`
- `music.png`
- `need-a-long-block.png`
- `needs-charging.png`
- `paradox.png`
- `passwrd.png`
- `pipe.png`
- `recharge.png`
- `solar.png`
- `storage.png`
- `sun-rising.png`
- `taken-sheep.png`

</details>

<details>
<summary><b>retro/</b> — 8 files</summary>

- `gnu-bg2.png`
- `gruvbox-dark-blue.png`
- `gruvbox-dark-rainbow.png`
- `linux-retro.jpg`
- `mario-fail.jpg`
- `pacman-grid.png`
- `pong.png`
- `snake.png`

</details>

<details>
<summary><b>collections/doctor-who/</b> — 11 files</summary>

- `alldoctors.jpg`
- `dalek.jpg`
- `tardis2.jpg`
- `tardisblack.jpg`
- `tardis.jpg`
- `tardis.png`
- `tardisstars.jpg`
- `tenth.jpg`
- `the-police-box-1.png`
- `travelsintime.png`
- `trustme.jpg`

</details>

<details>
<summary><b>collections/stalenhag/</b> — 59 files</summary>

- `stalenhag-01.jpg`
- `stalenhag-02.jpg`
- `stalenhag-03.jpg`
- `stalenhag-04.jpg`
- `stalenhag-05.jpg`
- `stalenhag-06.jpg`
- `stalenhag-07.jpg`
- `stalenhag-08.jpg`
- `stalenhag-09.jpg`
- `stalenhag-10.jpg`
- `stalenhag-11.jpg`
- `stalenhag-12.jpg`
- `stalenhag-13.jpg`
- `stalenhag-14.jpg`
- `stalenhag-15.jpg`
- `stalenhag-16.jpg`
- `stalenhag-17.jpg`
- `stalenhag-18.jpg`
- `stalenhag-19.jpg`
- `stalenhag-20.jpg`
- `stalenhag-21.jpg`
- `stalenhag-22.jpg`
- `stalenhag-23.jpg`
- `stalenhag-24.jpg`
- `stalenhag-25.jpg`
- `stalenhag-26.jpg`
- `stalenhag-27.jpg`
- `stalenhag-28.jpg`
- `stalenhag-29.jpg`
- `stalenhag-30.jpg`
- `stalenhag-31.jpg`
- `stalenhag-32.jpg`
- `stalenhag-33.jpg`
- `stalenhag-34.jpg`
- `stalenhag-35.jpg`
- `stalenhag-36.jpg`
- `stalenhag-37.jpg`
- `stalenhag-38.jpg`
- `stalenhag-39.jpg`
- `stalenhag-40.jpg`
- `stalenhag-41.jpg`
- `stalenhag-42.jpg`
- `stalenhag-43.jpg`
- `stalenhag-44.jpg`
- `stalenhag-45.jpg`
- `stalenhag-46.jpg`
- `stalenhag-47.jpg`
- `stalenhag-48.jpg`
- `stalenhag-49.jpg`
- `stalenhag-50.jpg`
- `stalenhag-51.jpg`
- `stalenhag-52.jpg`
- `stalenhag-53.jpg`
- `stalenhag-54.jpg`
- `stalenhag-55.jpg`
- `stalenhag-56.jpg`
- `stalenhag-57.jpg`
- `stalenhag-58.jpg`
- `stalenhag-59.jpg`

</details>
