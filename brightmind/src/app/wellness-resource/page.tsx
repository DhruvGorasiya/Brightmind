"use client";

import { useRouter } from "next/navigation";

interface Resource {
  title: string;
  description: string;
  link: string;
  category: string;
}

export default function WellnessResourcesPage() {
  const router = useRouter();

  const resources: Resource[] = [
    // Mental Health
    {
      title: "Crisis Text Line",
      description: "24/7 text support with trained crisis counselors",
      link: "https://www.crisistextline.org/",
      category: "Crisis Support"
    },
    {
      title: "National Suicide Prevention Lifeline",
      description: "24/7 support for people in distress",
      link: "https://988lifeline.org/",
      category: "Crisis Support"
    },
    // Meditation
    {
      title: "Headspace",
      description: "Guided meditation and mindfulness exercises",
      link: "https://www.headspace.com/",
      category: "Meditation"
    },
    {
      title: "Calm",
      description: "Sleep stories, meditation, and relaxation",
      link: "https://www.calm.com/",
      category: "Meditation"
    },
    // Exercise
    {
      title: "Nike Training Club",
      description: "Free workouts and fitness guidance",
      link: "https://www.nike.com/ntc-app",
      category: "Exercise"
    },
    // Therapy
    {
      title: "BetterHelp",
      description: "Online counseling and therapy services",
      link: "https://www.betterhelp.com/",
      category: "Therapy"
    }
  ];

  const categories = Array.from(new Set(resources.map(r => r.category)));

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white dark:from-gray-900 dark:to-gray-800 px-4 py-16">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl md:text-5xl font-bold mb-8 text-center bg-gradient-to-r from-blue-600 to-purple-600 text-transparent bg-clip-text">
          Wellness Resources
        </h1>

        <p className="text-center text-gray-600 dark:text-gray-300 mb-12">
          Find support and resources to help you on your wellness journey
        </p>

        {categories.map((category) => (
          <div key={category} className="mb-12">
            <h2 className="text-2xl font-bold mb-6 text-gray-800 dark:text-gray-100">
              {category}
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {resources
                .filter((resource) => resource.category === category)
                .map((resource) => (
                  <a
                    key={resource.title}
                    href={resource.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block p-6 bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-lg transition-shadow duration-300"
                  >
                    <h3 className="text-xl font-semibold text-blue-600 dark:text-blue-400 mb-2">
                      {resource.title}
                    </h3>
                    <p className="text-gray-600 dark:text-gray-300">
                      {resource.description}
                    </p>
                  </a>
                ))}
            </div>
          </div>
        ))}

        <button
          onClick={() => router.back()}
          className="mt-12 mx-auto block text-blue-600 dark:text-blue-400 hover:underline"
        >
          ← Go back
        </button>
      </div>
    </div>
  );
}