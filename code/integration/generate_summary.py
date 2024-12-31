def generate_support_summary(fused_representation):
    """
    Create a readable summary from the fused representation.
    """
    summary = []
    summary.append("=== Customer Support Interaction Summary ===")
    summary.append(f"Main Issues: {', '.join(fused_representation['main_issues'])}")
    summary.append(f"Text Sentiment: {fused_representation['text_sentiment']}")
    summary.append(f"Audio Sentiment: {fused_representation['audio_sentiment']}")
    summary.append("Keyframes: " + ", ".join(fused_representation['video_keyframes']))
    summary.append("Speaker Turns (secs): " + str(fused_representation['video_speaker_turns']))
    summary.append("Audio Transcript: " + fused_representation['audio_transcript'])
    summary_text = "\n".join(summary)
    return summary_text

# Example usage
if __name__ == "__main__":
    fused_data = {
        "main_issues": ["login issue", "error message"],
        "text_sentiment": "negative",
        "audio_sentiment": "frustrated",
        "video_keyframes": ["frame_1.jpg", "frame_2.jpg"],
        "video_speaker_turns": [5, 10],
        "audio_transcript": "I cannot log in due to an error message."
    }

    final_summary = generate_support_summary(fused_data)
    print(final_summary) 