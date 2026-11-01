# Reflex Arcade

A quick reaction-time game built with Flet. Wait for the signal to turn green, then tap as quickly as you can and see your reaction time in milliseconds.

## How to play

1. Tap **TAP TO START** to begin a round.
2. Wait for the green signal.
3. Tap as soon as it appears. Tapping early counts as a false start.
4. Check your latest time and personal best for the current session.
5. Start another round and try to improve your time.

The personal best is kept for the current session and resets when the app closes. Use the toggle in the top-right corner to switch between light and dark themes. The interface respects device safe areas so controls remain clear of system status and navigation elements.

## Publishing

Use **Publish** in Flet Studio to build or submit Reflex Arcade for a platform. Check the app version in `pyproject.toml` before a release; Flet Studio assigns build numbers automatically. Configure signing keys and store accounts in Studio, not in the app's source files.

### Android and Google Play

- Choose **Create APK** for a directly installable Android package. The action can also publish it to the app's download page.
- For Google Play, the package name must match `dev.flet.reflex_arcade`. Create the app in Play Console and upload its first app bundle (`.aab`) manually. After setup, connect Google Play in Flet Studio to publish releases to a track.
- Store listing text and artwork are kept by locale under `.store/google-play/`. Add the required screenshots and feature graphic before sending a listing.

### Apple App Store

Connect App Store Connect in Flet Studio and create the app there using the bundle ID shown in Publish settings. Then use the **TestFlight** or **App Store** actions to submit a build. Apple reviews App Store submissions. Listing text is stored under `.store/app-store/` by locale; add the screenshots required for the selected device family.

### Microsoft Store

Connect Partner Center in Flet Studio and select the app reserved there. Create the first Store package (`.msix`) and submit it manually through Partner Center; later updates can be submitted from Flet Studio. Microsoft Store listing text is stored under `.store/microsoft-store/` by locale.

For all stores, update the locale-specific listing files before sending a store listing. Store reviews and certification are handled by the platform and may take time.
